# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	b = eggs
	if b > 0 and b <=12:
		return 1
	elif b > 12 and b <= 24:
		return 2
	elif b > 24 and b <= 36:
		return 3
	elif b > 36:
		return 4
	else:
		return 0

