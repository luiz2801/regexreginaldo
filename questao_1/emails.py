from dataclasses import dataclass


@dataclass
class Email:
    pattern = r'^[a-z]+@[a-z]+\.(com\.br|br)$'
