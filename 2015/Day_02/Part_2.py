total_area = 0
a1 = 0
a2 = 0
a3 = 0
with open("Day_2.input") as f:
	for line in f:
		line = line.split("x")
		int_list = [int(i) for i in line]
		int_list.sort()
		a1 = 2*int_list[0]
		a2 = 2*int_list[1]
		a3 = int_list[0]*int_list[1]*int_list[2]
		total_area += a1 + a2 + a3

print total_area