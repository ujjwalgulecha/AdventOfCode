locations= [[0,0]]
cur_location_santa = [0,0]
cur_location_robot = [0,0]
num_houses = 1
turn = 0

f = open('Day_3.input', 'r')
while True:
    ch=f.read(1)
    if not ch: 
    	break
    if ch == '>':
        if turn == 0:
            cur_location_santa = [cur_location_santa[0] + 1,cur_location_santa[1]]
            if cur_location_santa not in locations:
                locations.append(cur_location_santa)
                num_houses +=1
        else:
            cur_location_robot = [cur_location_robot[0] + 1,cur_location_robot[1]]
            if cur_location_robot not in locations:
                locations.append(cur_location_robot)
                num_houses +=1

    elif ch == '^':
        if turn == 0:
    	   cur_location_santa = [cur_location_santa[0],cur_location_santa[1] + 1]
    	   if cur_location_santa not in locations:
                locations.append(cur_location_santa)
                num_houses +=1
        else:
            cur_location_robot = [cur_location_robot[0],cur_location_robot[1] + 1]
            if cur_location_robot not in locations:
                locations.append(cur_location_robot)
                num_houses +=1

    elif ch == '<':
        if turn == 0:
        	cur_location_santa = [cur_location_santa[0] - 1, cur_location_santa[1]]
        	if cur_location_santa not in locations:
        		locations.append(cur_location_santa)
        		num_houses +=1
        else:
            cur_location_robot = [cur_location_robot[0] - 1, cur_location_robot[1]]
            if cur_location_robot not in locations:
                locations.append(cur_location_robot)
                num_houses +=1

    else:
        if turn == 0:
        	cur_location_santa = [cur_location_santa[0],cur_location_santa[1] - 1]
        	if cur_location_santa not in locations:
        		locations.append(cur_location_santa)
        		num_houses +=1
        else:
            cur_location_robot = [cur_location_robot[0],cur_location_robot[1] - 1]
            if cur_location_robot not in locations:
                locations.append(cur_location_robot)
                num_houses +=1
    if turn == 0:
        turn = 1
    else:
        turn = 0

print num_houses
