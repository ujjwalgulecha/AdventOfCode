start = "1113222113"
temp = start
iterations = 40
i = 0

while i<iterations:
	j = 0
	temp2 = temp
	temp=""
	while j<len(temp2):
		c = temp2[j]
		ct = 1
		while j+1 <len(temp2) and c == temp2[j+1]:
			ct+=1
			j+=1
		temp+= str(ct) + str(c)
		j+=1
	i+=1

print len(temp)
