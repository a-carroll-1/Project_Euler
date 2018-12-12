"""
The sum of the squares of the first ten natural numbers is,

1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import timeit

tic = timeit.default_timer()

def sum_of_squares(n):
    """ Return the sum of squares in range n + 1 """
    j = 0
    for i in range(n + 1):
        j += i ** 2
    return j


def square_of_sums(n):
    """ Return the square of the sums in range n + 1 """
    j = 0
    return(sum([i for i in(range(n + 1))]) ** 2)

n = 100
print(square_of_sums(n) - sum_of_squares(n))
toc = timeit.default_timer()
print(toc - tic)
