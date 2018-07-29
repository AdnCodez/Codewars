# 5 kyu / Longest Common Subsequence
# Details
#   https://www.codewars.com/kata/longest-common-subsequence

from itertools import chain, combinations


def lcs(x, y):
    def power_set(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    var1 = (list(map(''.join, power_set(x))))
    var2 = (list(map(''.join, power_set(y))))
    ls = []
    for i in var1:
        if i in var2:
            ls.append(i)

    return max(ls, key=len)
