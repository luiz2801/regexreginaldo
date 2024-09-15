from cpf import validate_cpf


def test_cpf_success():
    batch = ["000.000.000-00",
             "123.456.789-10",
             "111.222.333-44",
             "109.876.543-21"]
    
    for cpf in batch:
        assert validate_cpf(cpf) == True


def test_cpf_failure():
    batch = ["000.000.000.00",
             "12345678910",
             "111-222-333-44",
             "109.876.543-134",
             "1091.2876.5431-34"]
    
    for cpf in batch:
        assert validate_cpf(cpf) == False
