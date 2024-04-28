from typing import Union


class Item:
    """Class Item is used to store data about an item.


    Attributes
    ----------

    all_items : List[Items]
        A List of all items which are available.
    capacity : int
        A maximum capacity of the knapsack.
    chosen_items : List[Items]
        A List of the chosen items to fill the knapsack.
    total_value : int
        A resulting maximum value that we obtain when knapsack is filled.


    Methods
    -------

    __len__()
        Returns number of uniq items in the knapsack.
    __str__()
        Returns a string representation of the filled knapsack.
    __getitem__()
        Returns item from filled knapsack by its index.
    collect_answers()
        Returns List of chosen items. This function uses result_matrix to form List of answers.
    fill()
        Fills the knapsack. This function solves the knapsack problem.

    """

    def __init__(
        self, name: Union[str, int], weight: int = 1, value: int = 1, quantity: int = 1
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
