from collections import defaultdict

replacements = defaultdict(list)
inp = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

with open("Day_19.input") as f:
	for line in f:
		data = line.strip().split()
		replacements[data[0]].append(data[2])

values = set()

for i in xrange(len(inp)):
	if inp[i] in replacements:
		for value in replacements[inp[i]]:
			new_values = inp[:i] + value + inp[i+1:]
			values.add(new_values)
	if i < len(inp) - 1: 
		two_letters = inp[i] + inp[i+1]
		if two_letters in replacements:
			for value in replacements[two_letters]:
				new_values = inp[:i] + value + inp[i+2:]
				values.add(new_values)
print len(values)