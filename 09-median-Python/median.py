# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	m = len(a)
	if m==0:
		return None
	a.sort()
	if m%2 == 0:
		median1 = a[m//2]
		# print(median1)
		median2 = a[m//2 -1]
		# print(median2)
		median = (median1+median2)/2
	else:
		median = a[m//2]
	return (median)