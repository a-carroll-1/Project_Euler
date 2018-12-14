"""
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
# 0.0026634719979483634 on Repl.it
import timeit


start = timeit.default_timer()
# We are going to make a list of 200 elements that will contain all the ways to make 200.
# Elements 0 and 2 will end up being 1, as there is only 1 way to make 200 with 200 and 199
# coins. Element 2 and 3 will be 2 because there are 2 ways to make 200 with 1 and 2 pence 
# coins. 
ways = [0] * 201
ways[0] = 1

# Iterate through the list by the coin size
for x in [1,2,5,10,20,50,100,200]:
    for i in range(x, 201):
        ways[i] += ways[i-x]
print(ways[200])
print(timeit.default_timer() - start)
