def find_word(data):
    for word in data:
        for i in range(len(word)):
            for j in range(26):
                changed = word
                changed = list(changed)
                changed[i] = chr(97 + j)
                changed = ''.join(changed)
                if changed in data and changed != word:
                    return changed[0:i] + changed[i+1:]


with open("input2.txt") as f:
    data = f.readlines()
    word = find_word(data)
    print word
