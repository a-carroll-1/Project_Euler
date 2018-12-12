"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
# 55.854559015017 on Repl.it first draft
# 1.7744522660505027 on Repl.it second draft
import math
import timeit


tic = timeit.default_timer()


def sieve_of_Eratosthenes(n):
    """ Return an n length list of sequential prime numbers """
    prime = [True for i in range(n + 1)] 
    p = 2
    while p * p <= n: 
        if prime[p]: 
            for i in range(p * 2, n+1, p): 
                prime[i] = False
        p += 1
    
    primes = []
    for p in range(2, n): 
        if prime[p]: 
            primes.append(p)
    
    return primes


print(sum(sieve_of_Eratosthenes(2000000)))
toc = timeit.default_timer()
print(toc - tic)
