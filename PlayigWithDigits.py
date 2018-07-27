# 6 kyu / Playing with digits
# Details
# https://www.codewars.com/kata/playing-with-digits/train/python


def dig_pow(n, p):
    n_str = str(n)
    p_list = list(range(p, len(n_str) + p))
    p_index = 0
    ls = []
    total = 0
    for j in n_str:
        res = int(j) ** p_list[p_index]
        ls.append(res)
        p_index += 1
    for i in ls:
        total += i
    if total % n == 0:
        return total // n
    else:
        return -1


print(dig_pow(46288, 3))
