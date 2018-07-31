# 7 kyu / Get the Middle Character
# Details
#   https://www.codewars.com/kata/get-the-middle-character


def gimme(input_array):
    sorted_array = sorted(input_array)
    sorted_array.pop(2)
    sorted_array.pop(0)
    val = sorted_array[0]
    return input_array.index(val)
