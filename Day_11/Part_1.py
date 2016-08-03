inp = "hxbxwxba"

flag = True


def process_word(inp):
	flag1 = False

	#Requirement1
	i = 0
	while i < len(inp) - 2:
		if ord(inp[i])+ 1 == ord(inp[i+1])  and ord(inp[i+1]) + 1 == ord(inp[i+2]) and inp[i]!=inp[i+2]:
			flag1 = True
			break
		else:
			i+=1
			flag1 = False

	if flag1 == False:
		return False

	#Requirement 2
	for i in inp:
		if i == 'i' or i == 'o' or i == 'l':
			return False

	ct = 0
	done = []
	i = 0
	#Requirement3
	while i < len(inp)-1:
		if inp[i] == inp[i+1] and inp[i] not in done:
			ct+=1
			done.append(inp[i])
			i+=2
		else:
			i+=1

	if ct < 2:
		return False

	return True

def next_word(inp):
	i = len(inp) - 1
	string  = ""

	while i>=0:
		if inp[i] == 'z':
			string+='a'
			i-=1
		else:	
			string+= chr(ord(inp[i]) + 1)
			i-=1
			break
	
	temp = inp[:i+1]
	string+= temp[::-1]
	return string[::-1]

while flag:
	inp = next_word(inp)
	if process_word(inp):
		flag = False
print inp
