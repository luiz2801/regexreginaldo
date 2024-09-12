import re

alfabeto = ("+", "-")
vazio = "ε"

def numeros(num):
    pattern = r'^(([+\-][0-9]*)|ε|([+\-][0-9]*\.[0-9]*))'
    a = r'^([+\-][0-9]+(\.[0-9]+)?|ε)$'
    if re.match(a, num):
        return 1
    return 0


a = "+ε"

print(numeros(a))
