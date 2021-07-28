# Write the function alternatingSum(a) that takes a list of numbers and returns the 
# alternating sum (where the sign alternates from positive to negative or vice versa). 
# For example, alternatingSum([5,3,8,4]) returns 6 (that is, 5-3+8-4). If the list is empty, return 0.




def fun_alternatingsum(a): 
	bh=len(a)
	sum=0
	for i in range(bh):
		if i%2==0:
			sum=sum+a[i]
		else:
			sum=sum-a[i]
	return sum

	


