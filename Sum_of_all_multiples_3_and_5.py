# 7 kyu / Sum of all the multiples of 3 or 5
# Details
#   https://www.codewars.com/kata/sum-of-all-the-multiples-of-3-or-5/train/python


def find(n):
    var = 0
    result = 0
    while var <= n:
        if var % 3 == 0 or var % 5 == 0:
            result += var
        var += 1
    return result


print(find(5))
