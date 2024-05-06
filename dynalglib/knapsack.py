from typing import List
from dynalglib.item import Item
from dynalglib.utils import generate_matrix


class Knapsack:
    """Class Knapsack is used to solve the Knapsack problem.


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
    _collect_answers()
        Returns List of chosen items. This function uses result_matrix to form List of answers.
    fill()
        Fills the knapsack. This function solves the knapsack problem.


    Example
    -------

    >>> from dynalglib import Knapsack
    >>> from dynalglib import Item
    >>> item1 = Item(name="apple", weight=2, value=3, quantity=6)
    >>> item2 = Item(name="pineapple", weight=4, value=8, quantity=3)
    >>> item3 = Item(name="kiwi", weight=3, value=6, quantity=3)
    >>> knapsack = Knapsack(items=[item1, item2, item3], capacity=10)
    >>> knapsack.fill()
    >>> print(knapsack.total_value) # prints max value that we obtain
    >>> print(knapsack) # prints which items we choose

    """

    def __init__(self, items: List[Item], capacity: int) -> None:
        self.all_items = items
        self.capacity = capacity
        self.chosen_items = list()
        self.total_value = 0

    def __len__(self) -> int:
        """Returns number of uniq items in the knapsack.

        Parameters
        ----------
        None

        Returns
        -------
        int
            A number of uniq items in the knapsack.
        """

        return len(self.chosen_items)

    def __str__(self) -> str:
        """Returns a string representation of the filled knapsack.

        Parameters
        ----------
        None

        Returns
        -------
        str
            A string representation of the filled knapsack.
        """

        return "\n".join(item.__str__() for item in self.chosen_items)

    def __getitem__(self, key: int) -> Item:
        """Returns item from filled knapsack by its index.

        Parameters
        ----------
        key: int
            An index of the desired item.

        Returns
        -------
        Item
            An item from filled knapsack by its index.
        """

        return self.chosen_items[key]

    def _collect_answers(self, result_matrix: List[List[int]]) -> List[Item]:
        """Returns List of chosen items. This function uses result_matrix to form List of answers.

        Parameters
        ----------
        result_matrix : List[List[int]]
            A two-dimensional List of maximum value and quntity of each item on each iteration.

        Returns
        -------
        List[Item]
            A list of chosen items.
        """

        result_List: List = []
        taken_quantity_sum: int = 0
        for i in range(len(result_matrix) - 1, -1, -1):
            if i == len(result_matrix) - 1:
                result_List.append(result_matrix[i][len(result_matrix[i]) - 1])
                taken_quantity_sum += (
                    self.all_items[i].weight
                    * result_matrix[i][len(result_matrix[i]) - 1][1]
                )
            else:
                result_List.append(
                    result_matrix[i][(len(result_matrix[i]) - 1 - taken_quantity_sum)]
                )
                taken_quantity_sum += (
                    self.all_items[i].weight
                    * result_matrix[i][len(result_matrix[i]) - 1 - taken_quantity_sum][
                        1
                    ]
                )

        result_List.reverse()

        items_info = []
        for index_of_item, answer in enumerate(result_List):
            if answer[1] > 0:
                items_info.append(
                    (
                        self.all_items[index_of_item].name,
                        self.all_items[index_of_item].weight,
                        self.all_items[index_of_item].value,
                        answer[1],
                    )
                )
        items = [
            Item(name=name, weight=weight, value=value, quantity=quantity)
            for name, weight, value, quantity in items_info
        ]

        return items

    def fill(self) -> None:
        """Fills the knapsack. This function solves the knapsack problem.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        ROWS = len(self.all_items)
        COLS = self.capacity + 1
        matrix = generate_matrix(rows=ROWS, cols=COLS)
        matrix = [[[None, None] for _ in range(COLS)] for _ in range(ROWS)]
        for index_row, row in enumerate(matrix):
            a = [
                min(
                    self.all_items[index_row].quantity,
                    i // self.all_items[index_row].weight,
                )
                for i in range(COLS)
            ]
            for index_col, col in enumerate(row):
                if index_row == 0:
                    col[0] = self.all_items[index_row].value * a[index_col]
                    col[1] = a[index_col]
                else:
                    results = []
                    for i in range(index_col + 1):
                        value = (
                            self.all_items[index_row].value * a[i]
                            + matrix[index_row - 1][index_col - i][0]
                        )
                        results.append(value)
                    max_in_tmp = max(results)
                    col[0] = max_in_tmp
                    col[1] = a[results.index(max_in_tmp)]
        self.chosen_items = self._collect_answers(matrix)
        self.total_value = sum([i.value * i.quantity for i in self.chosen_items])
