# 7 kyu / Categorize New Member
# Details
#   https://www.codewars.com/kata/categorize-new-member


def open_or_senior(data):
    result = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result


print(open_or_senior([[4, 22], [55, 21], [19, -2], [104, 20]]))
