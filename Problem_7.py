"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
import math
import timeit

tic = timeit.default_timer()
def is_prime(num):
    """ Return True if the number is Prime, False if it is composite. """
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

li = [2]
i = 0
while len(li) <= 10001:
    if is_prime(i):
        li.append(i)
    i += 1

print(li[-1])
toc = timeit.default_timer()
print(toc - tic)
