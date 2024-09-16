from dataclasses import dataclass


@dataclass
class RealNumber:
    pattern = r'^([+\-]?[0-9]+(\.[0-9]+)?)$'
