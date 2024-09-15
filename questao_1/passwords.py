import re


look_ahead_digits = r"(?=.*[0-9])"
look_ahead_capital_letters = r"(?=.*[A-Z])"
optional_lowercase_letters = r"(?:[a-z])?"

pattern = r"{}{}({}|[A-Z]|[0-9]){{8,}}".format(
     look_ahead_capital_letters,
     look_ahead_digits,
     optional_lowercase_letters,
)

compiled_pattern = re.compile(pattern)


def validate_password(password: str) -> bool:
    if compiled_pattern.match(password):
         return True
    
    return False
