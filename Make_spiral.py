# 3 kyu / Make a spiral
# Details
#   https://www.codewars.com/kata/make-a-spiral


def spiralize(n):
    if n == 0:
        return []

    grid_box = [[0] * n for _ in range(n)]
    grid_box[0] = [1] * n

    s = n - 1
    var1x, var1y = 0, n - 1
    var2x, var2y = 1, 0

    while s > 0:
        for i in range(2 if s > 1 else 1):
            for j in range(s):
                var1x, var1y = var1x + var2x, var1y + var2y
                grid_box[var1x][var1y] = 1
            var2x, var2y = var2y, -var2x
        s -= 2

    return grid_box


print(spiralize(5))
