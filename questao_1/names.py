from dataclasses import dataclass


@dataclass
class Name:
   pattern = r"^([A-Z][a-z]+)\s(?:[A-Z][a-z]+\s)?([A-Z][a-z]+)$"
