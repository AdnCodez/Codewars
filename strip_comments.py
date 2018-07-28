# 4 kyu / Strip Comments
# Details
#   https://www.codewars.com/kata/strip-comments/python


def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)
