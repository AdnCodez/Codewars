# 8 kyu / Reversed Strings
# Details
#   Complete the solution so that it reverses the string value passed into it.
# solution('world') # returns 'dlrow'


def solution(strng):
    result = ''
    if len(strng) == 0:
        return result
    else:
        for i in range(1, len(strng)):
            result += strng[-i]
        result += strng[0]
        return result


print(solution('world'))


# OR


def solution(strng):
    return strng[::-1]


print(solution('world'))
