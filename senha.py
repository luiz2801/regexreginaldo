import re

def psswrd(senha):
    pattern = r'^[a-z0-9A-Z]{8,}$'
    if re.match(pattern, senha):
        return 1
    return 0 

a = "aA280119"

print(psswrd(a))