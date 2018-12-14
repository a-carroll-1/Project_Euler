"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
# 0.07853122400410939 on Repl.it
import timeit
import itertools


start = timeit.default_timer()
seed = range(0, 10)
target = 1000000
# itertools.permutation will generate all perms in lexicographic order.
# islice grabs an element from a generator without converting to a list
answer = list(itertools.islice(itertools.permutations(seed, len(seed)), target - 1, target))
# we get a list of ints. Convert to list of strings and join.
# this whole process could be simplified by just providing the seed as a string. 
print(''.join([str(i) for i in answer[0]]))
print(timeit.default_timer() - start)
