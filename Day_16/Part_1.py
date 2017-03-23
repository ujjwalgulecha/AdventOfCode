from collections import defaultdict

types = ['children', 'cats', 'samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes']
aunt = {'children' : 3, 'cats' : 7, 'samoyeds' : 2, 'pomeranians' : 3, 'akitas' : 0, 'vizslas' : 0, 'goldfish' : 5, 'trees' : 3, 'cars' : 2, 'perfumes' : 1}

with open("Day_16.input") as f:
	index = 1
	for line in f:
		data = line.strip().split(",")
		fname =  data[0].split(":")[1]
		fvalue = int(data[0].split(":")[2])
		tempAunt = dict.fromkeys(types)
		tempAunt[fname.strip()] = fvalue
		for d in data[1:]:
			fname, fvalue = d.split(':')
			tempAunt[fname.strip()] = int(fvalue)
		flag = 0
		for key, value in aunt.iteritems():
			if tempAunt[key] == None:
				continue
			elif tempAunt[key] != value:
				flag = 1
				break
		if flag == 0:
			break
		index+=1

print index


