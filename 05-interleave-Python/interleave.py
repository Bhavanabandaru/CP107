# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	a=0
	b=0
	x=""
	if len(s1)>len(s2):
		b=len(s2)
	else:
		b=len(s1)
	while(a<b):
		x=x+s1[a]+s2[a]
		a+=1
	if b==len(s1):
		x=x+s2[b:]
	else:
		x=x+s1[b:]
	return x
	