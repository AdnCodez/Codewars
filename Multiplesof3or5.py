# 6 kyu / Multiples of 3 or 5
# Details
#   https://www.codewars.com/kata/multiples-of-3-or-5/python


def solution(number):
    res = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            res.append(i)
    return sum(res)


print(solution(10))
