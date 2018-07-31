# 6 kyu / Persistent Bugger.
# Details
#  Write a function, persistence, that takes in a positive parameter num and returns its multiplicative
#  persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
#  https://www.codewars.com/kata/persistent-bugger/train/python


import functools


def persistence(n):
    cnt = 0
    while n > 9:
        n = functools.reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        cnt += 1

    return cnt


print(persistence(999))
