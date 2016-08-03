#Read some hints for this one
import re

with open('Day_12.input') as f:
    inp = f.read()

print(sum(int(x) for x in re.findall(r'(-?\d+)', inp)))