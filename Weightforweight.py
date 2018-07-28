# 5 kyu / Weight for weight
# Details
#   https://www.codewars.com/kata/weight-for-weight


def digit_sum(s):
    n = s.split()
    rs = []
    for i in range(len(n)):
        rs.append(sum(int(i) for i in n[i]))
    return rs


def order_weight(strng):
    w = sorted(strng.split())
    sorted_w = sorted(w, key=digit_sum)
    return ' '.join(sorted_w)
