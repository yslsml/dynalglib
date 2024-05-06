from typing import List


def generate_matrix(rows: int = 5, cols: int = 5) -> List[List[int]]:
    """Returns a zero matrix (two-dimensional List) of a given size.

    Parameters
    ----------
    rows : int, optional
        A number of rows in matrix, by default 5.
    cols : int, optional
        A number of colomns in matrix, by default 5.

    Returns
    -------
    List[List[int]]
        A two-dimensional List representing a zero matrix of a given size.
    """

    matrix = [[0] * cols for _ in range(rows)]
    return matrix
