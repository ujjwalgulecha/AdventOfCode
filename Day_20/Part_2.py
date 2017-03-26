import math

inp = 36000000

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def find_sum(num):
	fac = factors(num)
	sumi = 0
	for f in fac:
		if num/f <= 50:
			sumi+= f*11
	return sumi

i = 1
while True:
	if find_sum(i) >= inp:
		break
	i+=1

print i
