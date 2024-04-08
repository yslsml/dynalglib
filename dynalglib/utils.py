def generate_matrix(rows: int = 5, cols: int = 5) -> list[list[int]]:
    """Returns a zero matrix (two-dimensional list) of a given size

    Parameters
    ----------
    rows : int, optional
        A number of rows in matrix, by default 5
    cols : int, optional
        A number of colomns in matrix, by default 5

    Returns
    -------
    list[list[int]]
        A two-dimensional list representing a zero matrix of a given size
    """

    # Инициализация матрицы нулями
    matrix = [[0] * cols for _ in range(rows)]
    return matrix
