# 6 kyu / Format a string of names like 'Bart, Lisa & Maggie'.
# Details
#   https://www.codewars.com/kata/format-a-string-of-names-like-bart-lisa-and-maggie/python


def namelist(names):
    ls = []
    for i in names:
        for j in i:
            ls.append(i[j])
    if len(ls) == 1:
        return ls[0]
    elif len(ls) == 0:
        return ''
    else:
        str1 = ', '.join(str(e) for e in ls[:-1])
        str2 = ''.join(str(e) for e in ls[-1:])
        return '{0} & {1}'.format(str1, str2)


print(namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]))
