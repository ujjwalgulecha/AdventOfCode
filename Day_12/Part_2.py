#Read some hints for this one
import json
import re

with open('Day_12.input') as f:
    red_filter = lambda x: {} if 'red'  in x.values() else x
    inp = json.load(f, object_hook=red_filter)
    print(sum(int(x) for x in re.findall(r'(-?\d+)', str(inp))))