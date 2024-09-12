import re



def cpf(cadastro):
    pattern = r'^[0-9]{3}+\.[0-9]{3}+\.[0-9]{3}+\-[0-9]{2}$'
    if re.match(pattern, cadastro):
        return 1
    return 0

a = ""

print(cpf(a))