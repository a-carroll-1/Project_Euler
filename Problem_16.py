"""
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
"""
# 0.04874122503679246 on Repl.it
import timeit


start = timeit.default_timer()
n = 2 ** 1000
n = list(str(n))
n = [int(i) for i in n]
print(sum(n))
print(timeit.default_timer() - start)

# Unreadable one-liner, but faster
# 0.00019766890909522772 on Repl.it
start = timeit.default_timer()
print(sum([int(i) for i in list(str(2 ** 1000))]))
print(timeit.default_timer() - start)
