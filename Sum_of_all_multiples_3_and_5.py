# 7 kyu / Sum of all the multiples of 3 or 5
# Details
# Your task is to write function findSum.
# Upto and including n, this function will return the sum of all multiples of 3 and 5.
# For example:
# findSum(5) should return 8 (3 + 5)
# findSum(10) should return 33 (3 + 5 + 6 + 9 + 10)
# https://www.codewars.com/kata/sum-of-all-the-multiples-of-3-or-5/train/python


def find(n):
    var = 0
    result = 0
    while var <= n:
        if var % 3 == 0 or var % 5 == 0:
            result += var
        var += 1
    return result


print(find(5))
