# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.
def isPrime(x):
	if (x < 2):
		return False
	if (x == 2):
		return True
	if (x % 2 == 0):
		return False
	maxFactor = round(x**0.5)
	for factor in range(3,maxFactor+1,2):
		if (x % factor == 0):
			return False
	return True


def fun_hasnoprimes(l):
	# your code goes here
	for i in range (len(l)):
		for j in range (len(l[i])):
			if isPrime(l[i][j]):
				return False
	return True


