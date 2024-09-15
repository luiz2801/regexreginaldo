from regular_expressions import ValidPatterns
from fixtures import run_perfect_batch, run_error_batch


homo_parents = ["HH", "MM"]


def test_d():
    batch = ["hmhmhm", "mhmhmh", "hmhmmh", "mhmmhhm"]
    run_perfect_batch(ValidPatterns.letter_d, batch, homo_parents)


def test_d_failure():
    batch = ["", "mm", "mmh", "hhhm", "hmhmh", "hhmhmh", "mhmhmm"]
    run_error_batch(ValidPatterns.letter_d, batch, homo_parents)


def test_e():
    batch = ["hm", "hmhm", "hmhmhm", "mh", "mhmh", "mhmhmh"]
    run_perfect_batch(ValidPatterns.letter_e, batch, homo_parents)


def test_e_failure():
    batch = ["", "mm", "hh", "hmhh", "mhmm"]
    run_error_batch(ValidPatterns.letter_e, batch, homo_parents)


def test_f():
    batch = ["h", "m", "hm", "mh", "hmh", "mmhmhmm"]
    run_perfect_batch(ValidPatterns.letter_f, batch, homo_parents)

def test_f_failure():
    batch = ["", "hh", "mmhh", "mhmhhm", "hmhhm"]
    run_error_batch(ValidPatterns.letter_f, batch, homo_parents)