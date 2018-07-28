# 6 kyu / Roman Numerals Encoder
# Details
#   https://www.codewars.com/kata/roman-numerals-encoder


def solution(n):
    str_n = str(n)
    symbol_value = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    divided_n = []
    res = []

    for i in range(len(str_n)):
        divided_n.append(int(str_n[i] + '0' * (int(len(str_n)) - i - 1)))
    divided_n[:] = (value for value in divided_n if value != 0)

    for i in divided_n:
        if i in symbol_value.keys():
            # print(True)
            res.append(symbol_value[i])
        else:
            # print(False)
            if i / 100 == 9:
                res.append(symbol_value[1000 - i])
                res.append(symbol_value[i + 100])
            elif i / 100 in [6, 7, 8]:
                res.append(symbol_value[500])
                for l in range(int(str(i - 500)[0])):
                    res.append(symbol_value[100])
            if i / 100 == 4:
                res.append(symbol_value[500 - i])
                res.append(symbol_value[i + 100])
            elif i / 100 in [2, 3]:
                for l in range(int(i / 100)):
                    res.append(symbol_value[100])

            if i / 10 == 9:
                res.append(symbol_value[100 - i])
                res.append(symbol_value[i + 10])
            elif i / 10 in [6, 7, 8]:
                res.append(symbol_value[50])
                for l in range(int(str(i - 50)[0])):
                    res.append(symbol_value[10])
            if i / 10 == 4:
                res.append(symbol_value[50 - i])
                res.append(symbol_value[i + 10])
            elif i / 10 in [2, 3]:
                for l in range(int(i / 10)):
                    res.append(symbol_value[10])

            if i / 1 == 9:
                res.append(symbol_value[10 - i])
                res.append(symbol_value[i + 1])
            elif i / 1 in [6, 7, 8]:
                res.append(symbol_value[5])
                for l in range(int(str(i - 5)[0])):
                    res.append(symbol_value[1])
            if i / 1 == 4:
                res.append(symbol_value[5 - i])
                res.append(symbol_value[i + 1])
            elif i / 1 in [2, 3, 4]:
                for l in range(int(i / 1)):
                    res.append(symbol_value[1])

    return ''.join(res)


print(solution(1998))
