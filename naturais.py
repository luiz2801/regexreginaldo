import re

alfabeto = ("+", "-")
vazio = "ε"

def numeros(num):
    pattern = r'^(([+\-]\d*)|ε|([+\-]\d*\.\d))'.format(alfabeto)
    if re.match(pattern, num):
        return 1
    return 0


a = "-5.45"

print(numeros(a))
