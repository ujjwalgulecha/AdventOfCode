lights = [[0 for i in range(1000)] for j in range(1000)]

with open("Day_6.input") as f:
	for line in f:
		line = line.split(" ")
		if line[0] == "turn":
			start = [int(x) for x in line[2].split(",")]
			end = [int(x) for x in line[4].split(",")]
			if line[1] == "on":
				for i in range(start[0],end[0]+1):
					for j in range(start[1],end[1]+1):
						lights[i][j] +=1
			else:
				for i in range(start[0],end[0]+1):
					for j in range(start[1],end[1]+1):
						lights[i][j] = max(0,lights[i][j]-1)
		else:
			start = [int(x) for x in line[1].split(",")]
			end = [int(x) for x in line[3].split(",")]
			for i in range(start[0],end[0]+1):
					for j in range(start[1],end[1]+1):
						lights[i][j]+=2

total_bright = 0
for i in range(1000):
	for j in range(1000):
		total_bright+=lights[i][j]

print total_bright