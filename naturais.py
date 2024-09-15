import re


def numeros(num):
    a = r'^([+\-]?[0-9]+(\.[0-9]+)?|ε)$'
    if re.match(a, num) and (num!="-0"):
        return 1
    return 0



a = "3.1415"n

print(numeros(a))
