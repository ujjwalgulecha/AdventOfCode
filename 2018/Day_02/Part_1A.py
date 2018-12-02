with open("input1.txt") as f:
    data = f.readlines()
    twos = 0
    threes = 0

    for word in data:
        chars = {}
        two_flag = False
        three_flag = False
        for c in word:
            if c in chars:
                chars[c]+=1
            else:
                chars[c] = 1
        for key, val in chars.iteritems():
            if val == 2 and not two_flag:
                two_flag = True
                twos+=1
            if val == 3 and not three_flag:
                three_flag = True
                threes+=1

    checksum = twos*threes
    print checksum
