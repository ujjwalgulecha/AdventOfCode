matrix = [[0 for i in range(1500)] for j in range(1500)]
with open("input1.txt") as f:
    data = f.readlines()
    count = 0
    for dat in data:
        sample = dat.split(" ")
        coords = sample[2].split(",")
        x = int(coords[0])
        y = int(coords[1][:-1])
        sizes = sample[3].split("x")
        size_1 = int(sizes[0])
        size_2 = int(sizes[1])

        # 0 - not used at all
        # 1 => already counted
        # 2 - used by some claim
        for i in range(y, size_2 + y):
            for j in range(x, size_1 + x):
                if matrix[i][j] == 0:
                    matrix[i][j] = 2
                elif matrix[i][j] != 1:
                    matrix[i][j] = 1
                    count+=1
print count
