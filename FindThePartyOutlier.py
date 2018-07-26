# 6 kyu / Find The Parity Outlier
# Details
#   https://www.codewars.com/kata/find-the-parity-outlier/train/python


def find_outlier(integers):
    ls = []
    rs = []
    for i in integers:
        if i % 2 == 0:
            ls.append(i)
        else:
            rs.append(i)
    return min(ls, rs, key=len)[0]


print(find_outlier([160, 3, 1719, 19, 11, 13]))
