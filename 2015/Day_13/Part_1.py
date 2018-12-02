from itertools import permutations
from collections import defaultdict

people_set = set()
people_scores = defaultdict(dict)

with open("Day_13.input") as f:
	for line in f:
		data = line.split()
		happiness = int(data[3]) if data[2] == 'gain' else int(data[3])*-1
		people_set.add(data[0])
		people_set.add(data[10][:-1])
		people_scores[data[0]][data[10][:-1]] = happiness

maxi = float("-inf")
for permutation in permutations(people_set):
	cur = 0
	for person in range(len(permutation)):
		if person < len(permutation) - 1 :
			cur+= people_scores[permutation[person]][permutation[person+1]] + people_scores[permutation[person+1]][permutation[person]]
		else:
			cur+= people_scores[permutation[person]][permutation[0]] + people_scores[permutation[0]][permutation[person]]
	maxi = max(maxi, cur)

print maxi
