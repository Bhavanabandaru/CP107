# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def digit(m,n):
    x = 0
    co = 0
    while(n > 0):
        x = n % 10
        if(x == m):
            co += 1
        n = n // 10
    return co
def mostfrequentdigit(n):
	# your code goes here
    x = -1
    f = -1

    for i in range(0,10):
        co = digit(i,n)
        if(co > f):
            f = co
            x = i
    return x

	

	