from itertools import product

from regular_expressions import ValidPatterns
from fixtures import run_perfect_batch, run_error_batch


#TESTE DE ACERTOS
def test_g_success():
    parents = ["HM", "MH", "HH", "MM"]
    batch = ["m", "mm", "mmm", "h", "hh", "hmmm"]
    run_perfect_batch(ValidPatterns.letter_g, batch, parents)


def test_g_failure():
    parents = ["HM", "MH", "HH", "MM"]
    batch = ["", "mmh", "mhm", "hmm", "hmhmmmh"]
    run_error_batch(ValidPatterns.letter_g, batch, parents)