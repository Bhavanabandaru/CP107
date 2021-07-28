# fabricyards(inches)
# Fabric must be purchased in whole yards, so purchasing just 1 inch 
# of fabric requires purchasing 1 entire yard. With this in mind, 
# write the function fabricYards(inches) that takes the number of 
# inches of fabric desired, and returns the smallest number of whole 
# yards of fabric that must be purchased.

# fabricexcess(inches)
# Write the function fabricexcess(inches) that takes the number of 
# inches of fabric desired and returns the number of inches of excess 
# fabric that must be purchased (as purchases must be in whole yards).
# Hint: you may want to use fabricyards, which you just wrote!

import math
def fabricyards(inches):
	# Your code goes here...
	x = inches
	if x == 0:
		return 0    
	if(x < 36 and x > 0):
		return 1
	elif(x >= 36):
		v = x / 36
		return math.ceil(v)

def fabricexcess(inches):
	# Your code goes here...
	y = inches
	if y > 0 and y <= 36:
		g = 36 - y
		return g
	elif y > 36 and y <=72:
		x = 72 - y
		return x
	elif y > 72:
		z = 108 - y
		return z
	return 0
