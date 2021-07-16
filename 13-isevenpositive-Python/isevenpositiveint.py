# isevenpositiveint(x)
# Write the function isevenpositiveint(x) that takes an arbitrary value x, return True if it is an
# integer, and it is positive, and it is even (all 3 must be True), or False otherwise. Do not
# crashing if the value is not an integer. So, isevenpositiveint("yikes!") returns False (rather
# than crashing), and isevenpositiveint(123456) returns True.

def isevenpositiveint(x):
	# your code goes here
	a = x
	if (type(a) == int and a > 0 and a % 2 == 0):
		return True
	else:
		return False
	
