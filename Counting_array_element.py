# 7 kyu / Counting Array Elements
# Details
#   Write a function that takes an array and counts the number of each unique element present.
# https://www.codewars.com/kata/counting-array-elements/train/python


def count(array):
    dic = {}
    for i in array:
        dic[i] = array.count(i)
    print(dic)


print(count(['a', 'a', 'b', 'b', 'b']))
