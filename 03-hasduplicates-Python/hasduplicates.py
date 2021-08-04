# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	l = []
	for i in range(len(L)):
		for j in range(len(L[i])):
			if  (L[i][j]) not in l:
				l.append(L[i][j])
			else:
				return True
	return False
