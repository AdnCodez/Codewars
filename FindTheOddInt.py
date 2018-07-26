# 6 kyu / Find the odd int
# Details
# Given an array, find the int that appears an odd number of times.
# There will always be only one integer that appears an odd number of times.


def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


print(find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]))
