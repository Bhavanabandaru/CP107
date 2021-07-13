# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


def dicetoorderedhand(a, b, c):
	# your code goes here
	value1 = max(a,b,c) # it is to find the max value of the 3 nums 
	value3 = min(a,b,c) # it is to find the min value of the 3 nums 
	value2 = a+b+c-value1-value3 # it is to find the middle value of the 3 nums 
	value = value1*100 + value2*10 +value3 # it is to find the whole value in the form of whole num in an ordered form
	
	return value