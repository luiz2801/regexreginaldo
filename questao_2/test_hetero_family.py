from families_and_patterns import ValidPatterns
from fixtures import run_perfect_batch, run_error_batch


hetero_parents = ["HM", "MH"]


def test_a_success():
    batch = ["mm", "hmm", "mmhh", "hmhm", "hmhm", "mhmhmh", "mhhhm",
             "h",
             "hhm", "hmh", "mhh"]
    run_perfect_batch(ValidPatterns.letter_a, batch, hetero_parents)


def test_a_failure():
    batch = ["", "m"]
    run_error_batch(ValidPatterns.letter_a, batch, hetero_parents)


def test_b_success():
    batch = ["m", "mmm", "mmmmm", 
             "hm", "mh", "hmhmm", "mhmhm",
             "hhmhmhm"]
    run_perfect_batch(ValidPatterns.letter_b, batch, hetero_parents)


def test_b_failure():
    batch = ["", "mm", "mmmm", "mmmmmm"]
    run_error_batch(ValidPatterns.letter_b, batch, hetero_parents)


def test_c_success():
    batch = ["mh", "mmh", "mhh", "mmhh", "mhmhmh"]
    run_perfect_batch(ValidPatterns.letter_c, batch, hetero_parents)


def test_c_failure():
    batch = ["", "hm", "hh", "mm", "mhmhm", "hmhmh"]
    run_error_batch(ValidPatterns.letter_c, batch, hetero_parents)