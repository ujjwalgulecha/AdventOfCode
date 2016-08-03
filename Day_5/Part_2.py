def process(sentence):
	
	double_occur = False

	for i in range(len(sentence)-1):
		sub = sentence[i] + sentence[i+1]
		if sentence.count(sub) >=2 :
			double_occur = True

	if double_occur == False:
		return False

	second_cond = False
	for i in range(len(sentence)-2):
		if sentence[i] == sentence[i+2] and sentence[i]!=sentence[i+1]:
			second_cond = True

	if second_cond == False:
		return False

	return True

nice_count = 0

with open("Day_5.input") as f:
	for line in f:
		sentence = line
		if process(sentence) == True:
			nice_count+=1

print nice_count


