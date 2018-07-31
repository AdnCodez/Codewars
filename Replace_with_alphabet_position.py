# 6 kyu / Replace With Alphabet Position
# Details
#   https://www.codewars.com/kata/replace-with-alphabet-position/python


def alphabet_position(text):
    res = []
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    for i in text:
        for j in alphabets:
            if i in alphabets:
                index = alphabets.index(i) + 1
            else:
                return ''
        res.append(str(index))
    return ' '.join(res)


print(alphabet_position('adnan'))
