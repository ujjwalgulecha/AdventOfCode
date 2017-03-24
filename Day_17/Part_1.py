from itertools import combinations

buckets = []
bucket_capacity = 150

with open("Day_17.input") as f:
	for line in f:
		data = line.strip()
		buckets.append(int(data))

#In all sizes of combinations, find the sum of containers that equal to bucket capacity
print sum(1 for i in xrange(len(buckets)) for combination in combinations(buckets, i) if sum(combination) == bucket_capacity)