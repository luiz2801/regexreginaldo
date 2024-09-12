import re

from dataclasses import dataclass


@dataclass
class ValidPatterns:
    """casais heterossexuais com pelo menos duas filhas mulheres
    ou um filho homem, ou ainda pelo menos dois filhos homens
    e uma filha mulher
    """
    first = r"[HM][[h|m]*mm+]|h|[h|m]*[hhm]"
    second = r"[HM][h*m(mm)*]"
    third = r"[HM]m[m|h]*h$"
    fourth = r"(M{2}|H{2})[hm][h|m][hm]"
    fifth = r"(M{2}|H{2})((hm)+|(mh)+)"
    sixth = r"(M{2}|H{2})m*h(m+h)*|m+(h(m+h)*)*"
    seventh = r""


class Family:
    """Cria uma família sob o seguinte formato:
    \nH: Homem, M: Mulher, h: filho, m: filha
    
    \nA ordem de cada membro da família determina \
    a idade relativa do membro (somente dois \
    adultos e em primeiro lugar)
    """

    def __init__(self, family: str | None = None, pattern: str | None = None,) -> None:
        self.family = family
        self.pattern = pattern
        if family is not None:
            self.validate_family_format()

    def validate_family_format(self) -> str:
        compiled_pattern = re.compile(self.pattern)
        validation = compiled_pattern.search(self.family)
        if validation is None:
            raise ValueError(f'"{self.family}" não respeita o formato.')
        
        return f'A família "{self.family}" está no formato correto.'
