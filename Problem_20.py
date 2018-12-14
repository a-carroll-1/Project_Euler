"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

# 0.00015852499927859753 on Repl.it
import timeit
from math import factorial


start = timeit.default_timer()
n=100
# Unreadable one liner
print(sum([int(i) for i in list(str(factorial(n)))]))
print(timeit.default_timer() - start)

# More readable, slower performance
start = timeit.default_timer()
answer = factorial(n)
answer = list(str(answer))  # Convert to string, make a list
answer = [int(i) for i in answer]  # Convert the elements in the list to integer
print(sum(answer))
print(timeit.default_timer() - start)
