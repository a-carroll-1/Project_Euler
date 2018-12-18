"""
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

"""
Check GitHub for the excel document I used as an aid for developing this formula.

Where n = the dimensions of the square. 
n = 1 = 1
n = 3 = 25
n = 5 = 101
n = 6 = 261 

Note the delta between each number:
n = 1-2 delta = 24
n = 2-3 delta = 76
n = 3-4 delta = 160

I noted that the delta could be expressed as follows:
delta = (previous delta + 13 + 8 * (n - 2)) * 4
where n is the current iteration (3x3 = 0, 5x5 = 1, 7x7 = 2 and so on)
Note that this formula does not consider the 1x1 case. 

Iterating over a for loop makes this process academic. 

"""
# 0.010797207010909915 on Repl.it
import timeit


def spiral_diagonals(n):
    """ Return the sum of the diagonals from a n x n spiral """
    if n == 1:  # 1 is an edge case that is not expressed in the below formula
        return 1

    n = n // 2 + 1  # Convert to the total number of iterations. 
    diag_sum = 25  # start with the value given by n = 2 
    delta_factor = 6
    for i in range(2, (n)):
        delta_factor += 13 + (8 * (i-2))
        diag_sum += delta_factor * 4

    return diag_sum

start = timeit.default_timer()

n = 1001  # dimensions of the spiral box.
print(spiral_diagonals(n))
print(timeit.default_timer() - start)
