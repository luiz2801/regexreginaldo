import re


pattern = r'^([+\-]?[0-9]+(\.[0-9]+)?|ε)$'
compiled_pattern = re.compile(pattern)


def validate_real_numbers(real_number: str) -> bool:
    if compiled_pattern.match(real_number) and (real_number != "-0"):
        return True
    
    return False
