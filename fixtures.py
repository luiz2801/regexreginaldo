import pytest

from regular_expressions import Family


dummy_family = Family()


def concatenate_couple(couple: str, children: str) -> str:
    return couple + children


def run_perfect_batch(pattern: str, children_batch: list, couples: list):
    dummy_family.pattern = pattern
    for older in couples:
        for children in children_batch:
            concat_family = concatenate_couple(older, children)
            dummy_family.family = concat_family
            dummy_family.validate_family_format()


def run_error_batch(dummy_family: Family, batch: list):
    for family in batch:
        dummy_family.family = family

        with pytest.raises(ValueError):
            dummy_family.validate_family_format()