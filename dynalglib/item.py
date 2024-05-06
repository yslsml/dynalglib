from typing import Union


class Item:
    """Class Item is used to store data about an item.


    Attributes
    ----------

    name : Union[str, int]
        The name of the item.
    weight : int
        The weight of the item.
    value : int
        The value of the item.
    quantity : int
        The quantity of the item.


    Methods
    -------

    __str__()
        Returns a string representation of a class object.


    Example
    -------

    >>> from dynalglib import Item
    >>> my_item = Item(name="apple", weight=2, value=3, quantity=6)
    >>> print(my_item)

    """

    def __init__(
        self, name: Union[str, int], weight: int = 1, value: int = 1, quantity: int = 1
    ) -> None:
        self.name = name
        self.weight = weight
        self.value = value
        self.quantity = quantity

    def __str__(self) -> str:
        """Returns a string representation of a class object.

        Parameters
        ----------
        None

        Returns
        -------
        str
            A string representation of a class object.
        """

        return (
            "name={}".format(self.name).ljust(20)
            + " weight={}".format(self.weight).ljust(15)
            + " value={}".format(self.value).ljust(15)
            + " quantity={}".format(self.quantity).ljust(15)
        )
