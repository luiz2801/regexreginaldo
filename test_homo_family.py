import re
from regular_expressions import ValidPatterns
from fixtures import run_perfect_batch


homo_couples = ["HH", "MM"]

# TESTE DE ACERTOS
def test_d():
    batch = ["hmhmhm", "mhmhmh", "hmhmmh", "mhmmhhm"]
    run_perfect_batch(ValidPatterns.fourth, batch, homo_couples)

def test_e():
    batch = ["hm", "hmhm", "hmhmhm", "mh", "mhmh", "mhmhmh"]
    run_perfect_batch(ValidPatterns.fifth, batch, homo_couples)

def test_f():
    batch = ["h", "m", "hm", "mh", "hmh", "mmhmhmm"]
    run_perfect_batch(ValidPatterns.sixth, batch, homo_couples)

# def test_b():
#     batch = ["m", "mmm", "mmmmm", 
#              "hm", "mh", "hmhmm", "mhmhm",
#              "hhmhmhm"]
#     run_perfect_batch(ValidPatterns.second, batch, hetero_couples)


# def test_c():
#     batch = ["mh", "mmh", "mhh", "mmhh", "mhmhmh"]
#     run_perfect_batch(ValidPatterns.third, batch, hetero_couples)
