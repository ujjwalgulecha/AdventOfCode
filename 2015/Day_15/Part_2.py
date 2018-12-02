ing = []

with open("Day_15.input") as f:
	for line in f:
		data = line.split()
		dat = [int(data[2][:-1]), int(data[4][:-1]), int(data[6][:-1]), int(data[8][:-1]), int(data[10])]
		ing.append(dat)

max_score = float("-inf")
total_weight = 100

def get_score(i, j, k):
	rem = 100 - (i + j + k)
	mult = [i, j, k, rem]
	score = 1
	for x in range(len(ing[0])):
		sc = 0
		for y in range(len(ing)):
			sc+= (ing[y][x]* mult[y])
		if sc < 0:
			score = 0
		#Only count those which have calorie score == 500
		if x == 4 and sc == 500:
			return score
		score = score * sc
	return -1

for i in range(0, total_weight + 1):
	for j in range(0, total_weight - i +1):
		for k in range(0, total_weight - i - j + 1):
			max_score = max(max_score, get_score(i, j, k))
		
print max_score