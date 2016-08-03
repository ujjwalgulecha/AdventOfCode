no_of_char = 0
no_of_char_in_memory = 0


def process(sentence):
	count = 0
	i = 1
	while i < len(sentence) - 1:
		if sentence[i] == "\\":
			if sentence[i+1] == "x":
				i = i+4
				count+=1
				continue
			elif sentence[i+1] == '"' or sentence[i+1] == "\\":
				i = i+2
				count+=1
				continue
		else:
			count+=1
			i = i + 1
			continue
	return count

with open("Day_8.input") as f:
	for line in f:
		line = line.strip()
		no_of_char += len(line)
		no_of_char_in_memory += process(line)


print no_of_char
print no_of_char_in_memory
diff =  no_of_char - no_of_char_in_memory
print diff