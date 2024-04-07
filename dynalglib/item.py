from typing import Union


class Item:
    """Class Item is used to store data about an item."""

    def __init__(
        self,
        name: Union[str, int],
        weight: int = 1,
        value: int = 1,
        quantity: int = 1,
    ) -> None:
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = quantity

    def __str__(self) -> str:
        return (
            "name={}".format(self.name).ljust(20)
            + " weight={}".format(self.weight).ljust(15)
            + " value={}".format(self.value).ljust(15)
            + " quantity={}".format(self.quantity).ljust(15)
        )
