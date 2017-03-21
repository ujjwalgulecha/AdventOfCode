from collections import defaultdict
import math

seconds = 2503
max_answer = float("-inf")

deer = defaultdict(list)

with open("Day_14.input") as f:
	i = 0
	for line in f:
		data = line.split()
		speed = int(data[3])
		time = int(data[6])
		rest = int(data[13])
		deer[i].append(speed)
		deer[i].append(time)
		deer[i].append(rest)
		#distance
		deer[i].append(0)
		#points
		deer[i].append(0)
		i+=1

def get_distance(d, cur_time):
	speed = d[0]
	time = d[1]
	rest = d[2]
	distance = math.floor(float(cur_time)/(time+rest)) * (speed*time)
	remain_time = cur_time - (math.floor(float(cur_time)/(time+rest)) * (time+rest))
	if remain_time >= 0:
		if remain_time >= time and remain_time <= time+rest:
			distance+= (speed*time)
		elif remain_time < time:
			distance+= (speed*remain_time)
	return distance

for dist in range(1, seconds + 1):
	cur_max_dist = float("-inf")
	for i in range(len(deer)):
		deer[i][3] = get_distance(deer[i], dist)
		cur_max_dist = max(cur_max_dist, deer[i][3])
	for i in range(len(deer)):
		if deer[i][3] == cur_max_dist:
			deer[i][4]+=1
print max([x[4] for x in deer.values()])
