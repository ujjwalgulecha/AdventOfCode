from copy import copy, deepcopy

lights = []
with open("Day_18.input") as f:
	for line in f:
		data = line.strip()
		light_temp = list(data)
		lights.append(light_temp)

def getNeighbours(j, k, lights):
	dx = [0, 1, -1]
	dy = [0, 1, -1]
	neighbours = 0
	for x in dx:
		for y in dy:
			if j+x >= 0 and j+x < len(lights[0]) and k+y >= 0 and k+y < len(lights):
				if lights[j+x][k+y] == on and (x or y):
					neighbours+=1
	return neighbours

def number_of_lights_on():
	return sum(1 for i in xrange(len(lights[0])) for j in xrange(len(lights)) if lights[i][j] == on)




iterations = 100
on = '#'
off = '.'

#Corner lights on
lights[0][0] = on
lights[0][99] = on
lights[99][0] = on
lights[99][99] = on

for i in xrange(iterations):
	temp_lights = deepcopy(lights)
	for j in xrange(len(lights[0])):
		for k in xrange(len(lights)):
			neighbours = getNeighbours(j, k, lights)
			if lights[j][k] == off:
				if neighbours == 3:
					temp_lights[j][k] = on
				else:
					temp_lights[j][k] = off
			else:
				if neighbours == 2 or neighbours == 3:
					temp_lights[j][k] = on
				else:
					temp_lights[j][k] = off
	lights = deepcopy(temp_lights)
	lights[0][0] = on
	lights[0][99] = on
	lights[99][0] = on
	lights[99][99] = on

print number_of_lights_on()