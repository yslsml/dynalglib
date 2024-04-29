import random
from typing import List
from dynalglib.item import Item
from dynalglib.utils import generate_matrix


class Resource_Allocation:
    """Class Resource_Allocation is used to solve the Resource Allocation problem.


    Attributes
    ----------

    profit_matrix : List[List[int]]
        A matrix with profits of each company.
    invest_in_company : List[int]
        A list representing the amount we allocate to each company.
    max_profit : int
        A maximum profit that can be obtained.


    Methods
    -------

    __getitem__()
        Returns the amount that we allocate in company by its index.
    collect_answers()
        Returns list representing the amount we allocate to each company.
    solve()
        Solves the Resource Allocation problem.

    """

    def __init__(self, profit_matrix: List[List[int]]):
        self.profit_matrix = [[0] + row for row in profit_matrix]
        self.invest_in_company: List[int] = list()
        self.max_profit: int = 0

    def __getitem__(self, key: int) -> int:
        """Returns the amount that we allocate in company by its index.

        Parameters
        ----------
        key: int
            An index of the desired company.

        Returns
        -------
        int
            The amount that we allocate in desired company.
        """

        return self.invest_in_company[key]

    def _collect_answers(self, result_matrix: List[List[int]]) -> List[int]:
        """Returns list representing the amount we allocate to each company. This function uses result_matrix to form allocation list.

        Parameters
        ----------
        result_matrix : List[List[int]]
            A two-dimensional list of maximum profit and amount that could be allocated to each company on each iteration.

        Returns
        -------
        List[int]
            A list representing the amount we allocate to each company.
        """

        results: List = []
        taken_quantity_sum: int = 0

        for i in range(len(result_matrix) - 1, -1, -1):  # FROM LAST TO FIRST
            if i == len(result_matrix) - 1:
                results.append(result_matrix[i][len(result_matrix[i]) - 1])
                taken_quantity_sum += result_matrix[i][len(result_matrix[i]) - 1][1]
            else:
                results.append(
                    result_matrix[i][(len(result_matrix[i]) - 1 - taken_quantity_sum)]
                )
                taken_quantity_sum += result_matrix[i][
                    len(result_matrix[i]) - 1 - taken_quantity_sum
                ][1]

        results.reverse()
        return results

    def solve(self) -> None:
        """Solves Resource Allocation problem.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """

        ROWS = len(self.profit_matrix)
        COLS = len(self.profit_matrix[0])
        matrix = generate_matrix(rows=ROWS, cols=COLS)
        matrix = [[[None, None] for _ in range(COLS)] for _ in range(ROWS)]
        for index_row, row in enumerate(matrix):
            for index_col, col in enumerate(row):
                if index_row != 0:
                    results = []  # Создаем пустой список для хранения результатов
                    for i in range(index_col + 1):
                        # Вычисляем значение для текущего элемента генератора
                        value = (
                            self.profit_matrix[index_row][i]
                            + matrix[index_row - 1][index_col - i][0]
                        )
                        results.append(value)  # Добавляем значение в список
                    max_value = max(results)
                    col[0] = max_value
                    col[1] = results.index(max_value)
                else:
                    col[0] = self.profit_matrix[index_row][index_col]
                    col[1] = index_col
        answers = self._collect_answers(result_matrix=matrix)
        self.invest_in_company = [i[1] for i in answers]
        self.max_profit = answers[-1][0]

    @staticmethod
    def generate_random_profit_matrix(
        company_count: int = 5,
        max_investment: int = 10,
        min_profit: int = 1,
        max_profit: int = 12,
    ) -> List[List[int]]:

        matrix = generate_matrix(rows=company_count, cols=max_investment + 1)
        # Заполнение матрицы случайными расстояниями
        for i in range(company_count):
            for j in range(max_investment + 1):
                while True:
                    number = random.randint(min_profit, max_profit) if j != 0 else 0
                    if number == 0 or number not in matrix[i]:
                        matrix[i][j] = number
                        break
            matrix[i].sort()
        return matrix
