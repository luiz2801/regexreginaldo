import re


def validate_pattern(pattern: str, string_to_compare: str) -> bool:
    compiled_pattern = re.compile(pattern)
    if compiled_pattern.match(string_to_compare):
        return True
    
    return False
