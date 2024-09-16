import pytest

from families_and_patterns import Family


dummy_family = Family()


def concatenate_parents(parents: str, children: str) -> str:
    return parents + children


def run_perfect_batch(pattern: str, children_batch: list, parents: list):
    dummy_family.pattern = pattern
    for older in parents:
        for children in children_batch:
            concat_family = concatenate_parents(older, children)
            dummy_family.family = concat_family
            dummy_family.validate_family_format()


def run_error_batch(pattern: str, children_batch: list, parents: list):
    dummy_family.pattern = pattern
    for older in parents:
        for children in children_batch:
            dummy_family.family = concatenate_parents(older, children)
            
            with pytest.raises(ValueError):
                dummy_family.validate_family_format()
