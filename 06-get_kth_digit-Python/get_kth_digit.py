# Write the function getKthDigit(n, k) that takes 
# a possibly-negative int n and a non-negative int k, 
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0 



def fun_get_kth_digit(digit, k):
    a = digit
    if a < 0:
        a = a * -1
        return (a // (10 ** k)%10)
    elif a > 0:
        return (a // (10 ** k)%10)
    else:
        return 0

