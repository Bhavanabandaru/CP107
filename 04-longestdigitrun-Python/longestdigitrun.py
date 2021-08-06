# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	x = abs(n)
	ldRun = 1
	ld = x % 10
	a = 1
	ind = x
	cont = 0
	while(ind != 0):
		ind = ind // 10
		cont = cont + 1
	if(cont == 1):
		return 1
	
	for i in range(0,cont):
		l = x % 10
		x = x // 10
		m = x % 10
		if(l == m):
			a = a + 1
		elif(a > ldRun):
			ldRun = a
			ld = l
			a = 1
		elif(a == ldRun and a < ld):
			ld = l
			a = 1
		else:
			a = 1
	return ld