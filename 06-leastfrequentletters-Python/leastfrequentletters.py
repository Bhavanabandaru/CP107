# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	s=s.lower()
	cnt=0
	n=""
	for i in s:
		for j in s:
			if(i==j):
				cnt=cnt+1
		if (cnt==1):
			n=n+i
		cnt=0
	st=""
	for i in n:
		if(i.isalpha()):
			st=st+i
	if(len(s)==0):
		return""
	else:
		return''.join(sorted(st))
