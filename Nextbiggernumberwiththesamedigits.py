import itertools

def next_bigger(n):
    try:
        ls = []
        res = []
        for i in [a for a in itertools.permutations(str(n))]:
            ls.append(int(''.join(i)))

        for i in ls:
            if i > n:
                res.append(i)

        return min(res)

    except ValueError:

        return -1


def _next_permutation(array):
    i = max(i for i in range(1, len(array)) if array[i - 1] < array[i])
    j = max(j for j in range(i, len(array)) if array[j] > array[i - 1])
    array[j], array[i - 1] = array[i - 1], array[j]
    array[i:] = reversed(array[i:])


def next_permutation(n):
    array = list(str(n))
    _next_permutation(array)
    return int(''.join(array))


# print(next_bigger())
print(next_permutation(59853))

# def nb(n):


#     ls = []
#     res = []
#     for i in reversed(str(n)):
#         ls.append(i)
#     cnt = 0
#     while cnt != len(ls):
#         if ls[cnt] > ls[cnt+1]:
#             res.append(ls[cnt+1])
#             res.append(ls[(cnt + 1) - 1])
#             res += ls[-2:]
#             cnt = len(ls)
#             return ''.join(reversed(res))
#         elif ls[cnt] < ls[cnt+1]:
#             res.append(ls[cnt])
#             if ls[cnt+1] > ls[cnt + 2]:
#                 res.append(ls[cnt + 2])
#                 res.append(ls[(cnt + 2) - 1])
#                 res += ls[-1:]
#                 cnt = len(ls)
#                 return ''.join(reversed(res))
#
#         else:
#             return -1
#
#
# print(nb(2071))
