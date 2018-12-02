with open("input1.txt") as f:
    data = f.readlines()
    count = 0
    for val in data:
        num = int(val[1:])
        if val[0] == '-':
            num = num * -1
        count+=num
print count
