# 7 kyu / Speed Control
# Details
#   https://www.codewars.com/kata/speed-control


def gps(s, x):
    if len(x) > 1:
        average_hourly_speed = []
        index = 0
        for i in range(len(x) - 1):
            var = (x[index + 1] - x[index]) / (s / 3600)
            index += 1
            average_hourly_speed.append(var)
        return int(max(average_hourly_speed))
    else:
        return 0


print(gps(18, [0.0, 0.01, 0.36, 0.6, 0.84, 1.05, 1.26, 1.47, 1.68, 1.89, 2.1, 2.31, 2.52, 2.73, 2.94, 3.15, 4]))
