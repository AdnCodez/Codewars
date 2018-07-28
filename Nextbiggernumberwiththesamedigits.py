# 4 kyu / Next bigger number with the same digits
# Details
#   https://www.codewars.com/kata/next-bigger-number-with-the-same-digits


def next_bigger(n):
    arr = [i for i in str(n)]
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return -1
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[len(arr) - 1: i - 1: -1]
    return int(''.join(arr))
