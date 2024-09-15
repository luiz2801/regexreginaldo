from passwords import Password
from validate_patterns import validate_pattern


def test_password_success():
    batch = ["abcABC01",
             "D3dEe4Ff",
             "GHIJKL689",
             "7m8NO9P10MH"]
    
    for password in batch:
        assert validate_pattern(Password.pattern, password) == True


def test_password_failure():
    batch = ["abcABCDEF",
             "ghi",
             "klmnopqr123",
             "12345678910"]
    
    for password in batch:
        assert validate_pattern(Password.pattern, password) == False
