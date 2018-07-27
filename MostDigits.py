# 7 kyu / Most digits
# Details
#   Find the number with the most digits.
# If two numbers in the argument array have the same number of digits, return the first one in the array.


def find_longest(data):
    for i in data:
        longest = str(max(data))
        num_digits = len(longest)
        if len(str(i)) == num_digits:
            return i


print(find_longest([1, 10999, 100, 20000]))
