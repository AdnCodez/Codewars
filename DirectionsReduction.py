# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# NS = ["NORTH", "SOUTH"]
# EW = ["EAST", "WEST"]
def fun(a, NS=["NORTH", "SOUTH"], EW=["EAST", "WEST"]):
    for elem in range(0, len(a), 2):
        var = (a[elem:elem + 2])
        if var == NS or var == EW:
            for i in range(0, len(NS)):
                f = a.remove(NS[i])
                # a.remove(NS[1])
                f = a.remove(EW[i])
                # a.remove(EW[1])
    return a
    # while var == NS or var == EW:
    #     fun(a)
    # return a


print(fun(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# for x in var:
#     for i in range(len(NS)):
#         if x != NS[i]:
#             print(x)

# if NS in a:
#     print(True)

'''
# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# EW = ["EAST", "WEST"]
# for n in range(0, len(a)):
#     print(a[n: n + 2])

    # for x in a[n: n + 2][::2]:
    #     print(x)
    #


def fun(l, sl):

    return [x for x in [l[n: n + 2] for n in range(0, len(l))[::2]]]


print(fun(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "SOUTH"], ["NORTH", "SOUTH"]))


# for n in range(0,len(l))[::2]:
#     x = l[n:n+2]
#     for i in x:
#         if i != sl:


#             print(i)
'''


def dirReduc(arr):
    north = 0
    south = 0
    east = 0
    west = 0
    for x in arr:
        if x == ["NORTH"]:
            north += 1
        elif x == ["SOUTH"]:
            south += 1
        elif x == ["EAST"]:
            east += 1
        elif x == ["WEST"]:
            west += 1
    if north == south and east != west:
        if east > west:
            return ["EAST"]
        elif west > east:
            return ["WEST"]
        else:
            return ["EAST", ["WEST"]
            if west == east and north != south:
                if
            south > north:
            return ["SOUTH"]
        elif north > south:
        return ["NORTH"]

else:
return arr


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


def dirReduc(arr):
    dir = " ".join(arr)
    dir2 = dir.replace("NORTH SOUTH", '').replace("SOUTH NORTH", '').replace("EAST WEST", '').replace("WEST EAST", '')
    dir3 = dir2.split()
    return dirReduc(dir3) if len(dir3) < len(arr) else dir3


opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}


def dirReduc(plan):
    new_plan = []
    for d in plan:
        if new_plan and new_plan[-1] == opposite[d]:
            new_plan.pop()
        else:
            new_plan.append(d)
    return new_plan
