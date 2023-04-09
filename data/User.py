import dataclasses


@dataclasses.dataclass
class User:
    subjects: tuple
    firstname: str
    lastname: str
    email: str
    phone: str
    address: str
    state: str
    city: str

