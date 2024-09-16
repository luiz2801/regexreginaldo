from dataclasses import dataclass


@dataclass
class CPF:
    pattern = r'^[0-9]{3}+\.[0-9]{3}+\.[0-9]{3}+\-[0-9]{2}$'
