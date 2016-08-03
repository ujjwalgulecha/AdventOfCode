no_of_char = 0
no_of_char_in_memory = 0
def process(sentence):
	count = 0
	i = 0
	while i < len(sentence):
		if sentence[i] == '"':
			count+=2
			i+=1
		elif sentence[i] == "\\":
			count+=2
			i+=1
		else:
			count+=1
			i+=1

	return count

with open("Day_8.input") as f:
	for line in f:
		line = line.strip()
		no_of_char += len(line)
		no_of_char_in_memory += process(line) + 2 #+2 for the opening and closing quotes


print no_of_char
print no_of_char_in_memory
diff = no_of_char_in_memory - no_of_char
print diff
