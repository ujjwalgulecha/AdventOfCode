locations= [[0,0]]
cur_location = [0,0]
num_houses = 1

f = open('Day_3.input', 'r')
while True:
    ch=f.read(1)
    if not ch: 
    	break

    if ch == '>':
    	cur_location = [cur_location[0] + 1,cur_location[1]]
    	if cur_location not in locations:
    		locations.append(cur_location)
    		num_houses +=1

    elif ch == '^':
    	cur_location = [cur_location[0],cur_location[1] + 1]
    	if cur_location not in locations:
    		locations.append(cur_location)
    		num_houses +=1

    elif ch == '<':
    	cur_location = [cur_location[0] - 1, cur_location[1]]
    	if cur_location not in locations:
    		locations.append(cur_location)
    		num_houses +=1

    else:
    	cur_location = [cur_location[0],cur_location[1] - 1]
    	if cur_location not in locations:
    		locations.append(cur_location)
    		num_houses +=1

print num_houses

