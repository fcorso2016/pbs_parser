from typing import TypedDict

class Item(TypedDict):
    name: str
    name_plural: str
    pocket: int
    price: int
    field_use: str
    flags: list[str]
    description: str
