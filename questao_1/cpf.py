import re


pattern = r'^[0-9]{3}+\.[0-9]{3}+\.[0-9]{3}+\-[0-9]{2}$'
compiled_pattern = re.compile(pattern)


def validate_cpf(cpf: str) -> bool:
    if compiled_pattern.match(cpf):
        return True
    
    return False