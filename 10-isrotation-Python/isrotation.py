# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	x=str(x)
	y=str(y)
	
	if len(x)!=len(y) or len(x)==0 or len(y)==0:
		return False
	
	for i in range(len(x)):
		x=x[1:]+x[0]
		print(x)
		if x==y:
			return True
	return False
