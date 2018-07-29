# 4 kyu / Twice linear
# Details
#   https://www.codewars.com/kata/twice-linear/python

from collections import deque


def dbl_linear(n):
    var = 1
    count = 0
    queue1 = deque([])
    queue2 = deque([])
    while True:
        if count >= n:
            return var
        queue1.append(2 * var + 1)
        queue2.append(3 * var + 1)
        var = min(queue1[0], queue2[0])
        if var == queue1[0]:
            var = queue1.popleft()
        if var == queue2[0]:
            var = queue2.popleft()
        count += 1
