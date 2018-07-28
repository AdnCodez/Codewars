# 5 kyu / Directions Reduction
# Details
#   https://www.codewars.com/kata/directions-reduction


def dirReduc(arr):
    opposite = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    stack = []
    for i in arr:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[len(stack) - 1] == opposite[i]:
                stack.pop()
            else:
                stack.append(i)
    return stack
