from date_and_time import validate_date_and_time


def test_date_and_time_success():
    batch = ["07/09/2001 01:00:00",
             "23/12/2014 12:35:49",
             "01/01/1986 00:01:01",
             "12/10/0020 23:57:33"]
    
    for date_and_time in batch:
        assert validate_date_and_time(date_and_time) == True


def test_date_and_time_failure():
    batch = ["07/09/2001 1:1:1",
             "00/00/0000 00:00:00",
             "010/119/86 00:01:01",
             "12/10/002023:57:33"]
    
    for date_and_time in batch:
        assert validate_date_and_time(date_and_time) == False
