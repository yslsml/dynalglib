from dynalglib.item import Item
from dynalglib.utils import create_martix


class Knapsack:
    """_summary_"""

    def __init__(self, items: list[Item], capacity: int) -> None:
        self.all_items = items
        self.capacity = capacity
        self.filled_knapsack = list()
        self.total_value = 0

    def __len__(
        self,
    ) -> int:
        """_summary_

        Returns
        -------
        int
            _description_
        """

        return len(self.filled_knapsack)

    def __str__(
        self,
    ) -> str:
        """_summary_

        Returns
        -------
        str
            _description_
        """

        return "\n".join(item.__str__() for item in self.filled_knapsack)

    def __getitem__(self, key):
        return self.filled_knapsack[key]

    def collect_answers(self, result_matrix: list[list]) -> list[Item]:
        """_summary_

        Parameters
        ----------
        result_matrix : list[list]
            _description_

        Returns
        -------
        list[Item]
            _description_
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
        """_summary_"""

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
        self.filled_knapsack = self.collect_answers(matrix)
        self.total_value = sum([i.value * i.quantity for i in self.filled_knapsack])
