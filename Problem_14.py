"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
# If we create a dictionary to store existing collatz numbers you can minimize calculations
# 8.107472852920182 on Repl.it
import timeit


def generate_chain(n):
    """ Appends to the chain dictionary """
    if n in chain:
        return chain[n]
    if n % 2 != 0:  # Odd cases
        chain[n] = 1 + generate_chain(3 * n + 1)
    else:
        chain[n] = 2 + generate_chain(n // 2)
    
    return chain[n]

start = timeit.default_timer()
chain = {1: 1}
longest_chain = 0
answer = 1

for i in range(50000, 1000000):
    contender = generate_chain(i)
    if contender > longest_chain:
        longest_chain = contender
        answer = i

print(answer)
print(timeit.default_timer() - start)
# 70.29239535599481 on Repl.it
# Brute Force approach. Calculates the collatz value too many times. 
"""
def collatz(n):
    j = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        j += 1
    return j


start = timeit.default_timer()
greatest = [0, 0]
for i in range(500000, 1000000):
    contender = collatz(i)
    if contender > greatest[0]:
        greatest = contender, i

print(greatest[1])
print(timeit.default_timer() - start)
"""
