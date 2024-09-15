from emails import validate_email


def test_email_success():
    batch = ["savio@email.br",
             "luiz@email.com.br",
             "joao@barbosa.br",
             "reginaldo@dossantos.com.br"]
    
    for email in batch:
        assert validate_email(email) == True


def test_email_failure():
    batch = ["savio@email.com",
             "s4v1o@email.com",
             "uiz@email.com.jp",
             "joao@antonio@.com",
             "@savio.com.br"
             "reginaldo_123@.com.br"]
    
    for email in batch:
        assert validate_email(email) == False
