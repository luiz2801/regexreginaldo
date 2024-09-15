from names import Name
from validate_patterns import validate_pattern


def test_name_success():
    batch = ["Savio Luiz Miranda",
             "Savio Miranda",
             "Luiz Gabriel",
             "Joao Antonio Barbosa"]
    for name in batch:
        assert validate_pattern(Name.pattern, name) == True


def test_name_failure():
    batch = ["Luiz G4briel Moreira",
             "joao antonio",
             "Savio luiz miranda",
             "Reginaldo"]
    for name in batch:
        assert validate_pattern(Name.pattern, name) == False
