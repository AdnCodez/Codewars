# 7 kyu / Vowel Count
# Details
#   Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.
# The input string will only consist of lower case letters and/or spaces.


def get_count(inputstr):
    cnt = 0
    for c in inputstr:
        if c in "ouiaeOUIAE":
            cnt += 1

    return cnt


print(get_count("abraocaodabra"))
