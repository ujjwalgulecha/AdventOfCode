from collections import defaultdict
import math

seconds = 2503
max_answer = float("-inf")

with open("Day_14.input") as f:
	for line in f:
		data = line.split()
		speed = int(data[3])
		time = int(data[6])
		rest = int(data[13])
		distance = math.floor(float(seconds)/(time+rest)) * (speed*time)
		remain_time = seconds - (math.floor(float(seconds)/(time+rest)) * (time+rest))
		if remain_time >= 0:
			if remain_time >= time and remain_time <= time+rest:
				distance+= (speed*time)
			elif remain_time < time:
				distance+= (speed*remain_time)
		max_answer = max(distance, max_answer)
print int(max_answer)