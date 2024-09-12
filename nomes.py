import re

def validate(nome_completo):

    pattern = r"^([A-Z][a-z])+(\s[A-Z][a-z]+)?\s([A-Z][a-z])+$"

    # Verifica se o nome completo corresponde à expressão regular
    if re.match(pattern, nome_completo):
      return 1

    return 0
    

a = "Ada Lovelace"
print(validate(a))