from dataclasses import dataclass


@dataclass
class Password:
     _look_ahead_digits = r"(?=.*[0-9])"
     _look_ahead_capital_letters = r"(?=.*[A-Z])"
     _optional_lowercase_letters = r"(?:[a-z])?"

     pattern = r"{}{}({}|[A-Z]|[0-9]){{8,}}".format(
     _look_ahead_capital_letters,
     _look_ahead_digits,
     _optional_lowercase_letters,
     )
