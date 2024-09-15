from phone_number import validate_cellphone


def test_cellphone_success():
    batch = ["(91) 981692643",
             "(92) 98493-7538",
             "91 981692643"]
    
    for number in batch:
        assert validate_cellphone(number) == True


def test_cellphone_failure():
    batch = ["(91)981692643",
             "(92)58493-7538",
             "91981692643"]
    
    for number in batch:
        assert validate_cellphone(number) == False
