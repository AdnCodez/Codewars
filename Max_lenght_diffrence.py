# 7 kyu / Maximum Length Difference
# Details
#   https://www.codewars.com/kata/maximum-length-difference


def mxdiflg(a1, a2):
    ls = []
    ts = []
    if len(a1) == 0 or len(a2) == 0:
        return -1
    else:
        for i in a1:
            ls.append(len(i))

        for j in a2:
            ts.append(len(j))

        var1 = abs(min(ls) - max(ts))
        var2 = abs(max(ls) - min(ts))
        return max(var1, var2)
