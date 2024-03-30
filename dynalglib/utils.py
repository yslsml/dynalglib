from typing import Any


def create_martix(rows: int, colms: int, filler: Any = None):
    return [[filler.copy() for _ in range(colms)] for _ in range(rows)]
