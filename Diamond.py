# 6 kyu / Give me a Diamond
# Details
#   You need to return a string that displays a diamond shape on the screen using asterisk ("*") characters.


def diamond(n):
    if n % 2 != 0:
        count = 1
        while count != n + 2:
            print("{0:^{1}}".format("*" * count, n))
            count += 2
        count = n - 2
        while count >= 1:
            print("{0:^{1}}".format("*" * count, n))
            count -= 2
        return ''
    else:
        return None


print(diamond(9))
