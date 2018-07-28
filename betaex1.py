# Beta / Testing 1-2-3
# Details
#   https://www.codewars.com/kata/testing-1-2-3


def number(lines):
    ls = []
    for i_index, i in enumerate(lines):
        var = '{}: {}'.format(i_index + 1, i)
        ls.append(var)

    return ls


print(number(["a", "b", "c"]))
