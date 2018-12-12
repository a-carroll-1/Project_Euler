"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# Brute force 
# 0.7981928660301492 on Repl.it
tic = timeit.default_timer()
def is_palindrome(i):
    """ Return True if given integer is a palindrome """
    i = str(i)  # Convert to string so we can do list slicing
    if i == i[::-1]:
        return True
    else:
        return False

i = 100
j = 100
greatest = 0
while (i <= 999):
    while (j <= 999):
        product = i * j
        if (product > greatest and is_palindrome(str(product))):
            greatest = product
        j += 1
    j = 100
    i += 1
print(greatest)
toc = timeit.default_timer()
print(toc - tic)

# Optimizations
# Note that palindrome numbers are cleanly divisible by 11, so less numbers can be checked. 
# Start at 999 instead of 1, and check that the numbers being generated are not less than the largest palindrome currently found. 
# 0.001289136940613389 on Repl.it
import timeit

tic = timeit.default_timer()
def is_palindrome(i):
    """ Return True if given integer is a palindrome """
    i = str(i)  # Convert to string so we can do list slicing
    if i == i[::-1]:
        return True
    else:
        return False

greatest = 0
for i in range(999, 100, -1):
    if i % 11 == 0:  # Palindromes are always multiples of 11
        j = 999
        db = 1
    else:
        j = 990  # Largest number less than 999 and divisible by 11
        db = 11
    while j >= i:
        if i * j <= greatest:
            break
        if is_palindrome(i * j):
            greatest = i * j
        
        j = j - db

print(greatest)
toc = timeit.default_timer()
print(toc - tic)
