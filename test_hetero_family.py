from regular_expressions import ValidPatterns
from fixtures import run_perfect_batch


hetero_couples = ["HM", "MH"]

# TESTE DE ACERTOS
def test_a():
    batch = ["mm", "hmm", "mmhh", "hmhm", "hmhm", "mhmhmh", "mhhhm",
             "h",
             "hhm", "hmh", "mhh"]
    run_perfect_batch(ValidPatterns.first, batch, hetero_couples)


def test_b():
    batch = ["m", "mmm", "mmmmm", 
             "hm", "mh", "hmhmm", "mhmhm",
             "hhmhmhm"]
    run_perfect_batch(ValidPatterns.second, batch, hetero_couples)


def test_c():
    batch = ["mh", "mmh", "mhh", "mmhh", "mhmhmh"]
    run_perfect_batch(ValidPatterns.third, batch, hetero_couples)
