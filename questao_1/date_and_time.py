import re


pattern = r'^((0[1-9]|[12][0-9]|3[01])/([0][1-9]|1[0-2])/([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]|[0-9][1-9][0-9]{2}|[1-9][0-9]{3})\s([0-1][0-9]|[2][0-3])\:([0-5][0-9])\:([0-5][0-9]))$'

compiled_pattern = re.compile(pattern)


def validate_date_and_time(date_and_time: str) -> bool:
    if compiled_pattern.match(date_and_time):
        return True
    
    return False
