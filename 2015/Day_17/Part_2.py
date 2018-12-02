from itertools import combinations

buckets = []
bucket_capacity = 150
min_size = float("inf")

with open("Day_17.input") as f:
	for line in f:
		data = line.strip()
		buckets.append(int(data))

#Find the minimum number of buckets required
for i in xrange(len(buckets)):
	for combination in combinations(buckets, i):
		if sum(combination) == bucket_capacity and i <= min_size:
			min_size = i

#Find combinations of minimum size that have sum == bucket capacity
print sum(1 for combination in combinations(buckets, min_size) if sum(combination) == bucket_capacity)


