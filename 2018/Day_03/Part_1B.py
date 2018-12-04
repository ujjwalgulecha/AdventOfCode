from sets import Set
matrix = [[0 for i in range(1500)] for j in range(1500)]
with open("input2.txt") as f:
    data = f.readlines()
    ids_overlap = Set([])
    for dat in data:
        sample = dat.split(" ")
        coords = sample[2].split(",")
        x = int(coords[0])
        y = int(coords[1][:-1])
        sizes = sample[3].split("x")
        size_1 = int(sizes[0])
        size_2 = int(sizes[1])
        id = int(sample[0][1:])
        # 0 - not used at all
        # id - used by some claim
        for i in range(y, size_2 + y):
            for j in range(x, size_1 + x):
                if matrix[i][j] == 0:
                    matrix[i][j] = id
                else:
                    ids_overlap.add(id)
                    ids_overlap.add(matrix[i][j])
                    matrix[i][j] = id

for i in range(1, id + 1):
    if i not in ids_overlap:
        print i
        break
