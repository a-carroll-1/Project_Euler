"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
# Brute Force
# 30.323076730943285 on Repl.it
import timeit

tic = timeit.default_timer()

i = 0
factors = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]  # The smaller factors are unnecessary 
j = 20
while j > 10:
    i += 20  # 20 is the largest divisor, no reason to check numbers in between
    for j in factors:
        if i % j != 0:
            break

print(i)
toc = timeit.default_timer()
print(toc - tic)
