import re

from dataclasses import dataclass


@dataclass
class ValidPatterns:
    letter_a = r"^(HM|MH)([hm]*m[hm]*m+[hm]*|[hm]*h+[hm]*|[hm+][hm+][hm+][hm]*)$"
    letter_b = r"^(HM|MH)(h*mh*(mh*m)*h*)$"
    letter_c = r"^(HM|MH)m[hm]*h$"
    letter_d = r"^(M{2}|H{2})(hm|mh)(hm|mh|hh|mm)[hm]*(hm|mh)$"
    letter_e = r"^(M{2}|H{2})(hm+(hm)*|mh+(mh)*)$"
    letter_f = r"^(M{2}|H{2})([hm]|(m+h|m)+|(hm+)+|(m+h|hm+h)|(m+|hm+h))$"
    letter_g = r"^[HM][HM]([hm]|[hm][hm]|[hm]*mmm)$"


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
