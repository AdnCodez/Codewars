# 5 kyu / Best travel
# Details
#   https://www.codewars.com/kata/best-travel/python

import itertools


def choose_best_sum(t, k, ts):
    ls = []
    combinations = list(itertools.combinations(ts, k))
    if len(ts) <= 1:
        return None
    for i in combinations:
        sum_var = sum(i)
        if sum_var <= t:
            ls.append(sum_var)
    return max(sorted(ls), default=None)


print(choose_best_sum(163, 3, [50, 55, 56, 57, 58]))
