import re


pattern = r"^([A-Z][a-z]+)\s(?:[A-Z][a-z]+\s)?([A-Z][a-z]+)$"
compiled_pattern = re.compile(pattern)


def validate_names(full_name: str) -> bool:
    # Verifica se o nome completo corresponde à expressão regular
    if re.match(pattern, full_name):
       return True
    
    return False
