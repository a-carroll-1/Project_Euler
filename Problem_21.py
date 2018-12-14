"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
# Produces an incorrect answer, investigate 
# 
# 0.9906943599999067 on Repl.it
import timeit
from functools import reduce


def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if not n % i)))


def sum_of_factors(n):
    return sum(factors(n)) - n


amicables = set()
start = timeit.default_timer()
for i in range(2, 10000):
    b = sum_of_factors(i)
    if sum_of_factors(b) == i and b < 10000:
        amicables.add(i)

print(amicables)
print(sum(amicables))
print(timeit.default_timer() - start)
