import hashlib

num=1
while True:
	m = hashlib.md5()
	hash_string = "yzbqklnj" + str(num)
	m.update(hash_string)
	hash_value = m.hexdigest()
	first_five = hash_value[:5]
	if first_five == "00000":
		break
	num = num + 1

print hash_value
print num