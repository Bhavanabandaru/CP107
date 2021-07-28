# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).



def fun_nth_happy_prime(n):
	n = abs(n)
	count = -1
	i = 2
	while True:
		if is_prime(i) and is_happy(i):
			count += 1
		if count == n:
			break
		i += 1

	return i

def is_happy(n):
	while(1):
		if n == 1:
			return True
		if n == 4:
			return False
		else:
			n = sum_sqof_digits(n)

	return False

def sum_sqof_digits(n):
	sum = 0
	while n > 0:
		sum += (n % 10)**2
		n = n // 10
	return sum

def is_prime(n):
	if n < 2:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True

	