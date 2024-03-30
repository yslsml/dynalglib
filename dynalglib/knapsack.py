from dynalglib.item import Item
from dynalglib.utils import create_martix


class Knapsack:
    """Class Knapsack is used to solve the Knapsack problem.


    Attributes
    ----------

    all_items : Items
        list of all items which are available
    capacity : int
        maximum capacity of the knapsack
    chosen_items : list
        list of the chosen items to fill the knapsack
    total_value : int
        resulting maximum value that we obtain when knapsack is filled


    Methods
    -------

    __len__()
        Returns number of uniq items in the knapsack
    __str__()
        Returns a string representation of the filled knapsack
    __getitem__()
        Returns item from filled knapsack by its index
    collect_answers()
        Returns list of chosen items. This function uses result_matrix to form list of answers
    fill()
        Fills the knapsack. This function solves the knapsack problem

    """

    def __init__(self, items: list[Item], capacity: int) -> None:
        self.all_items = items
        self.capacity = capacity
        self.chosen_items = list()
        self.total_value = 0

    def __len__(
        self,
    ) -> int:
        """Returns number of uniq items in the knapsack

        Returns
        -------
        int
            number of uniq items in the knapsack
        """

        return len(self.chosen_items)

    def __str__(
        self,
    ) -> str:
        """Returns a string representation of the filled knapsack

        Returns
        -------
        str
            string representation of the filled knapsack
        """

        return "\n".join(item.__str__() for item in self.chosen_items)

    def __getitem__(self, key) -> Item:
        """Returns item from filled knapsack by its index

        Returns
        -------
        Item
            item from filled knapsack by its index
        """

        return self.chosen_items[key]

    def collect_answers(self, result_matrix: list[list]) -> list[Item]:
        """Returns list of chosen items. This function uses result_matrix to form list of answers

        Parameters
        ----------
        result_matrix : list[list]
            two-dimensional list of maximum value and quntity of each item on each iteration

        Returns
        -------
        list[Item]
            list of chosen items
        """

        result_list: list = []
        taken_quantity_sum: int = 0
        for i in range(len(result_matrix) - 1, -1, -1):  # FROM LAST TO FIRST
            if i == len(result_matrix) - 1:
                result_list.append(result_matrix[i][len(result_matrix[i]) - 1])
                taken_quantity_sum += (
                    self.all_items[i].weight
                    * result_matrix[i][len(result_matrix[i]) - 1][1]
                )
            else:
                result_list.append(
                    result_matrix[i][(len(result_matrix[i]) - 1 - taken_quantity_sum)]
                )
                taken_quantity_sum += (
                    self.all_items[i].weight
                    * result_matrix[i][len(result_matrix[i]) - 1 - taken_quantity_sum][
                        1
                    ]
                )

        result_list.reverse()

        items_info = []
        for index_of_item, answer in enumerate(result_list):
            if answer[1] > 0:
                items_info.append(
                    (
                        self.all_items[index_of_item].name,  # name
                        self.all_items[index_of_item].weight,  # weight
                        self.all_items[index_of_item].value,  # value
                        answer[1],  # quantity
                    )
                )
        items = [
            Item(name=name, weight=weight, value=value, quantity=quantity)
            for name, weight, value, quantity in items_info
        ]

        return items

    def fill(
        self,
    ) -> None:
        """Fills the knapsack. This function solves the knapsack problem"""

        ROWS = len(self.all_items)
        COLMS = self.capacity + 1
        # МОЖНО ПОПРОБОВАТЬ СДЕ"ЛАТЬ ОТДЕЛЬНЫЙ КЛАСС CELL, КОТОРЫЙ БУДЕТ ХРАНИТЬ ЗНАЧЕНИЕ ЯЧЕЙКИ
        matrix = create_martix(rows=ROWS, colms=COLMS, filler=[None, None])
        for index_row, row in enumerate(matrix):
            a = [
                min(
                    self.all_items[index_row].quantity,
                    i // self.all_items[index_row].weight,
                )
                for i in range(COLMS)
            ]
            for index_col, col in enumerate(row):
                if index_row == 0:
                    col[0] = self.all_items[index_row].value * a[index_col]
                    col[1] = a[index_col]
                else:
                    results = []  # Создаем пустой список для хранения результатов
                    for i in range(index_col + 1):
                        # Вычисляем значение для текущего элемента генератора
                        value = (
                            self.all_items[index_row].value * a[i]
                            + matrix[index_row - 1][index_col - i][0]
                        )
                        results.append(value)  # Добавляем значение в список
                    max_in_tmp = max(results)
                    col[0] = max_in_tmp
                    col[1] = a[results.index(max_in_tmp)]
        self.chosen_items = self.collect_answers(matrix)
        self.total_value = sum([i.value * i.quantity for i in self.chosen_items])
