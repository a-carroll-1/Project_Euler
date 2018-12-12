"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
# 55.854559015017 on Repl.it first draft
# 0.9198489129776135 on Repl.it second draft
import timeit

def sieve(n):
    is_prime = [True] * (n+1)  # list of Booleans, all set to True
    primes = [2]  # Start with 2. It's the first prime number and an oddball.

    # Prime numbers have to be odd, so start at 3 and increment by 2
    for p in range(3, n + 1, 2):
        if is_prime[p]:
            primes.append(p)

            # We know that multiples of a given prime are not prime so we set those
            # to false in our list of booleans. 
            for multiple in range(p * p, n + 1, p + p):
                is_prime[multiple] = False

    return primes


tic = timeit.default_timer()
print(sum(sieve(2000000)))
toc = timeit.default_timer()
print(toc - tic)
