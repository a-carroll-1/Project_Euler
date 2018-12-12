"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a ** 2 + b ** 2 = c ** 2
For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 5 ** 2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
# 0.27599609503522515 on Repl.it
import math
import timeit

tic = timeit.default_timer()
def pytha(a, b):
    """ 
    Given a, b return c from the following formula:
    a ** 2 + b ** 2 = c ** 2
    """
    c = math.sqrt((a ** 2) + (b ** 2))
    if int(c) - c == 0:  # Not sure how to use isInstance to check if 4.0 is an int -.-
        return int(c)
    else:
        return False

def list_product(li):
    """ Return the product of a list """
    r = 1
    for i in li:
        r *= i
    return r

found = False
for a in range(1, 332):  # 332 + 333 + 334 is the largest number under 1000
    if found:
        break
    # b could be an arbitraily large number, but the largest b possible is [1, 444, 445]
    for b in range(a + 1, 444):
        c = pytha(a, b)
        pytha_sum = a + b + c
        if pytha_sum > 1000:
            break
        if pytha_sum == 1000:
            found = [a, b, c]

print(list_product(found))
toc = timeit.default_timer()
print(toc - tic)  
