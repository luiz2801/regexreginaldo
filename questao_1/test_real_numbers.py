from real_numbers import validate_real_numbers


def test_real_number_success():
    batch = ["+12.0", "12.0", "-12.0", "999.99", "-123.456", "+3.4"]
    
    for real_number in batch:
        assert validate_real_numbers(real_number) == True


def test_real_number_failure():
    batch = ["+12.", "=12.0", "-1.2.0", ".99", "-1.", "+33,4"]
    
    for real_number in batch:
        assert validate_real_numbers(real_number) == False
