# 5 kyu / Base64 Encoding
# Details:
#   Create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII
#   character set.
#   https://www.codewars.com/kata/base64-encoding

from base64 import b64encode, b64decode


def to_base_64(string):
    return b64encode(string).rstrip('=')


def from_base_64(string):
    missing_padding = 4 - len(string) % 4
    if missing_padding:
        string += b'=' * missing_padding
    return b64decode(string)
