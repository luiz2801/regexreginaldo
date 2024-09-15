from names import validate_names


def test_name_success():
    batch = ["Savio Luiz Miranda",
             "Savio Miranda",
             "Luiz Gabriel",
             "Joao Antonio Barbosa"]
    for name in batch:
        assert validate_names(name) == True


def test_name_failure():
    batch = ["Luiz G4briel Moreira",
             "joao antonio",
             "Savio luiz miranda",
             "Reginaldo"]
    for name in batch:
        assert validate_names(name) == False
