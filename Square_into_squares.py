# 4 kyu / Square into Squares. Protect trees!
# Details
# https://www.codewars.com/kata/square-into-squares-protect-trees/train/python


def decompose(n):
    goal = 0
    result = [n]
    while result:
        current = result.pop()
        goal += current ** 2
        for i in range(current - 1, 0, -1):
            if goal - (i ** 2) >= 0:
                goal -= i ** 2
                result.append(i)
                if goal == 0:
                    result.sort()
                    return result
    return None


print(decompose(3232322))
