import re

def check_email(email):
    padrao = r'^[a-z0-9]+@[a-z0-9]+\.(com\.br|br)$'
    if re.match(padrao, email):
         return 1
    return 0

#alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789_-' 

a = "dfgn@a.br"

print(check_email(a))