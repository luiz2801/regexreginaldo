import re


pattern = r'^[a-z]+@[a-z]+\.(com\.br|br)$'
compiled_pattern = re.compile(pattern)


def validate_email(email: str) -> bool:
    if compiled_pattern.match(email):
         return True
    
    return False
