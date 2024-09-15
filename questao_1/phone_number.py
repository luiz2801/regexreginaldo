from dataclasses import dataclass


@dataclass
class PhoneNumber:
    pattern = r'^(\([0-9]{2}\)|[0-9]{2})\s9([0-9]{8}|[0-9]{4}\-[0-9]{4})$'
