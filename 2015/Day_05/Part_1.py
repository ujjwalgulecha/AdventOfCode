def process(sentence):
	bad_strings = ["ab","cd","pq","xy"]
	vowels = ["a","e","i","o","u"]
	for bad_string in bad_strings:
		if bad_string in sentence:
			return False

	vowel_count = 0
	for char in sentence:
		if char in vowels:
			vowel_count+=1

	if vowel_count < 3:
		return False

	for i in range(len(sentence)-1):
		if sentence[i] == sentence[i+1]:
			return True

	return False


nice_count = 0

with open("Day_5.input") as f:
	for line in f:
		sentence = line
		if process(sentence) == True:
			nice_count+=1

print nice_count


