"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
# Brute force (0.7981928660301492 on Repl.it)
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
