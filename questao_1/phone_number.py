import re


pattern = r'^(\([0-9]{2}\)|[0-9]{2})\s9([0-9]{8}|[0-9]{4}\-[0-9]{4})$'
compiled_pattern = re.compile(pattern)


def validate_cellphone(number: str) -> bool:
    if compiled_pattern.match(number):
        return True
    
    return False
