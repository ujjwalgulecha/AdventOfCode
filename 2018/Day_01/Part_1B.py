with open("input2.txt") as f:
    data = f.readlines()
    count = 0
    nums=[]
    for i in range(len(data)):
        val = data[i]
        num = int(val[1:])
        if val[0] == '-':
            num = num * -1
        nums.append(num)

    freqs = [0]
    flag = True
    while flag:
        i = 0
        while i < len(nums):
            count+=nums[i]
            if count in freqs:
                flag = False
                break
            else:
                freqs.append(count)
            i+=1
print count
