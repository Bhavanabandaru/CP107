# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def isTidy(n):
    a = n
    x = 0
    y = 0
    while a > 0:
        x = a % 10
        a = a //10
        y = a % 10
        if x < y:
            return False
    return n

def fun_nth_tidynumber(n):
    count =0
    x = 1
    while (count <= n):
        if (isTidy(x)):
            count = count + 1
        x += 1
    return x-1
