# # def lcs(x, y):
# #     result = ''
# #
# #
# # print(lcs('AGCAT', 'GAC'))
#
# x = 'BANANA'
# # x = 'ABCDEFG'
# # x = 'AGCAT'
#
# y = 'ATANA'
# # y = 'BCDGK'
# # y = 'GAC'
# ls = []
# ts = []
# res = ''
# count = 0
# count2 = 0
# for i in x:
#     ls.append(i)
# for j in y:
#     ts.append(j)
# while count != len(x):
#     if ts[count2] == x[count]:
#         res += ts[count2]
#         count2 += 1
#     else:
#         count += 1
#
# print(res)

# def lcs(x, y):
#     result = ''
#     ls = []
#     count = 0
#     while y[count] in y:
#         if y[count] in x:
#             ls.append(y[count])
#             count += 1
#         else:
#             count += 1
#
#     print(ls)
#
#
#
#
#
#
#
#
#
#
#
# print(lcs('BANANA', 'ATANA'))
# print(lcs('ABCDEFG', 'BCDGK'))
# print(lcs('AGCAT', 'GAC'))
# print(lcs('ANOTHETEST', 'NOTTEST'))
from itertools import chain, combinations

from itertools import chain, combinations
def lcs(x, y):
    def powerset(iterable):
        s = list(iterable)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    var1 = (list(map(''.join, powerset(x))))
    var2 = (list(map(''.join, powerset(y))))
    ls = []
    for i in var1:
        if i in var2:
            ls.append(i)

    return max(ls, key=len)


print(lcs('BANANA', 'ATANA'))


def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        lcs1 = lcs(x, y[:-1])
        lcs2 = lcs(x[:-1], y)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2


def lcs(x, y):
    res = []
    i = 0
    for item in y:
        if item in x[i:]:
            res += [item]
            i = x.index(item) + 1
    return "".join(res)


# remove duplicates from a string in python
# x = 'aabbccde'
# res = ''
# for i in x:
#     if i not in res:
#         res += i
# print(res)
def removeduplicate(x):
    res = ''
    res += (str(i) for i in x if i not in res)
    return res


print(removeduplicate('aabbccde'))

"""
def lcs(x, y):
    result = ''
    def rmduplicate(string):
        res = ''
        for i in string:
            if i not in res:
                res += i
        return res
    x = rmduplicate(x)       #Checkes the first property from wiki
    # y = rmduplicate(y)

    for j in y:
        for i in x:
            if j is i:
                result += str(j)
                # result = rmduplicate(result) #FALSE
    return result


print(lcs('AGCAT', 'GAC'))

"""
from itertools import combinations


def subsequences(s):
    """Returns set of all subsequences in s."""
    return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))


def lcs(x, y):
    """Returns longest matching subsequence of two strings."""
    return max(subsequences(x).intersection(subsequences(y)), key=len)
