import math
from itertools import combinations
#given boss stats
boss_hp = 103
boss_dmg = 9
boss_arm = 2

ct = 0

user_hp = 100

#cost, damage and armor respectively
weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]


max_gold = float("-inf")


def player_cost(weapon, armor, ring):
	#initializations
	ring_cost = sum(x[0] for x in ring)
	ring_dmg = sum(x[1] for x in ring)
	ring_armor = sum(x[2] for x in ring)

	cost = weapon[0] + armor[0] + ring_cost
	uhp = user_hp
	bhp = boss_hp

	player_arm = weapon[2] + armor[2] + ring_armor
	player_damage = weapon[1] + armor[1] + ring_dmg - boss_arm 
	boss_damage = boss_dmg - player_arm

	while uhp > 0 :
	    bhp -= max(1, player_damage)
	    if bhp <= 0:
	    	return float("-inf")
	    uhp -= max(1, boss_damage)
	return cost

#Trying each combination
for weapon in weapons:
	for armor in armors:
		for i in range(3):
			for ring in combinations(rings, i):
				cost_to_player = player_cost(weapon, armor, ring)
				if cost_to_player > max_gold:
						max_gold = cost_to_player
						stats = weapon, armor, ring


#no armor
for weapon in weapons:
	for i in range(3):
		for ring in combinations(rings, i):
			cost_to_player = player_cost(weapon, [0, 0, 0], ring)
			if cost_to_player > max_gold:
					max_gold = cost_to_player
					stats = weapon, armor, ring
	

print max_gold
print stats