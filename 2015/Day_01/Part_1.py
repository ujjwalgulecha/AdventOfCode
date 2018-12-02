floor = 0
with open("Day_1.input") as f:
	while True:
		c = f.read(1)
		if not c:
			print "Done"
			break
		if c == '(':
			floor+=1
		if c == ')':
			floor-=1
print floor
