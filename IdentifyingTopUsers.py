# 5 kyu / Identifying Top Users and their Corresponding Purchases On a Website
# Details
#   https://www.codewars.com/kata/identifying-top-users-and-their-corresponding-purchases-on-a-website

from collections import Counter


def id_best_users(*args):
    all_months_users = set.intersection(*(set(a) for a in args))
    count = Counter(x for sublist in list(args) for x in sublist)
    users = {}
    for key, value in count.items():
        if key in all_months_users:
            users.setdefault(value, []).append(key)
    return [[key, sorted(value)] for key, value in sorted(users.items(), reverse=True)]
