from collections import defaultdict
import itertools
cities = []

with open("Day_9.input") as f:
    for line in f:
        line = line.strip()
        data = line.split(" ")
        if data[0] not in cities:
            cities.append(data[0])
        if data[2] not in cities:
            cities.append(data[2])

cost_matrix = defaultdict(dict)

with open("Day_9.input") as f:
    for line in f:
        line = line.strip()
        data = line.split(" ")
        cost_matrix[data[0]][data[2]] = int(data[4])
        cost_matrix[data[2]][data[0]] = int(data[4])

perms = list(itertools.permutations(cities))

max = 0
min_path =[]
for permutation in perms:
    path = []
    sum = 0
    i = 0
    flag = 0
    while i < len(permutation)-1:
        if flag == 1:
            break
        try:
            sum+= cost_matrix[permutation[i]][permutation[i+1]]
            path.append(permutation[i])
            path.append(permutation[i+1])
            i+=1
        except KeyError,e:
            flag = 1
            continue
    if flag == 0 and sum>max:
        max = sum
        max_path = path

print max
print max_path  