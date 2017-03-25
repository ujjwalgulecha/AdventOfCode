from random import shuffle

molecule = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'

replacements = []

with open('Day_19.input') as f:
    for line in f:
    	data = line.strip()
        if '=>' in line:
            X, _, Y = data.split()
            replacements.append((X, Y))

count = shuffles = 0
mol = molecule
while len(mol) > 1:
    start = mol
    for X, Y in replacements:
        while Y in mol:
            count += mol.count(Y)
            mol = mol.replace(Y, X)

    if start == mol:
        shuffle(replacements)
        mol = molecule
        count = 0
        shuffles += 1

print count