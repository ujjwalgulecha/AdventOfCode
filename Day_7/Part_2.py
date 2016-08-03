#Assignments are 3 length
#NOT are 4 length
#AND, OR, LSHIFT and RSHIFT are 5 length

data = []
with open("Day_7_2.input") as f:
	for line in f:
		line = line.split(" ")
		data.append(line)

store={}
index = 0
#First evaluate the assignments and then need to do multiple passes to evaluate values
while True:
	index = 0
	loop = False
	for line in data:
		if len(line) == 3:
			if line[0].isdigit():
				store[line[2].strip()] = int(line[0])
				data.pop(index)
				loop = True
				break
		index+=1
	if loop == False:
		break

while len(data)>1:
	index = 0
	loop = False
	#print len(data)
	for line in data:
		#NOT
		if len(line) == 4:
			if line[1] in store:
				store[line[3].strip()] = ~store[line[1]]
				data.pop(index)
				break
			index+=1
		else:
			if line[0] in store and (line[1] == "LSHIFT" or line[1]=="RSHIFT"):
				if line[1] == "LSHIFT":
					store[line[4].strip()] = store[line[0]]<<int(line[2])
					data.pop(index)
					break
				else :
					store[line[4].strip()] = store[line[0]]>>int(line[2])
					
					data.pop(index)
					break
			elif line[0] in store and line[2] in store:
				if line[1] == "AND":
					store[line[4].strip()] = store[line[0]] & store[line[2]]
					data.pop(index)
					break
				else:
					store[line[4].strip()] = store[line[0]] | store[line[2]]
					data.pop(index)
					break
			elif (line[2] in store and line[0].isdigit()) or (line[0] in store and line[2].isdigit()):
				if line[1] == "OR":
					if line[0] in store:
						store[line[4].strip()] = store[line[0]] | int(line[2])
						data.pop(index)
						break
					else:
						store[line[4].strip()] = store[line[2]] | int(line[0])
						data.pop(index)
						break
				else:
					if line[0] in store:
						store[line[4].strip()] = store[line[0]] & int(line[2])
						data.pop(index)
						break
					else:
						store[line[4].strip()] = store[line[2]] & int(line[0])
						data.pop(index)
						break
			
			index+=1
for line in data:
	store[line[2].strip()] = store[line[0]]
	data.pop(index)
for key,value in store.items():
	print key,value