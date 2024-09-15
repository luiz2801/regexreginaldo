from phone_number import PhoneNumber
from validate_patterns import validate_pattern


def test_cellphone_success():
    batch = ["(91) 981692643",
             "(92) 98493-7538",
             "91 981692643"]
    
    for number in batch:
        assert validate_pattern(PhoneNumber.pattern, number) == True


def test_cellphone_failure():
    batch = ["(91)981692643",
             "(92)58493-7538",
             "91981692643"]
    
    for number in batch:
        assert validate_pattern(PhoneNumber.pattern, number) == False
