import random
from typing import List
from dynalglib.utils import generate_matrix


class TSP:
    """Class TSP is used to solve the Traveling Salesman Problem.


    Attributes
    ----------

    distance_matrix : List[List[int]]
        A two-dimensional List (symmetric matrix) of distances between cities.
    min_distance : int
        The minimum distance for which all cities can be visited.
    path : List[int]
        A List of cities which represent the shortest possible path.


    Methods
    -------

    __str__()
        Returns a string representation of the minimum distance and resulting path.
    _dfs()
        Depth-First Search algorithm to find the shortest path in the TSP.
    solve()
        Solves the Traveling Salesman Problem.
    generate_random_distance_matrix()
        Returns two-dimensional List of random distances between cities.


    Example
    -------

    >>> from dynalglib import TSP
    >>> distance_matrix = TSP.generate_random_distance_matrix(city_count=5)
    >>> tsp = TSP(distance_matrix=distance_matrix)
    >>> tsp.solve()
    >>> print(tsp.min_distance) # prints minimum possible distance
    >>> print(tsp.path) # prints the best path

    """

    def __init__(self, distance_matrix: List[List[int]]) -> None:
        self.distance_matrix: List[List[int]] = distance_matrix
        self.min_distance: int = None
        self.path: List[int] = None

    def __str__(self) -> str:
        """Returns a string representation of the minimum distance and resulting path.

        Parameters
        ----------
        None

        Returns
        -------
        str
            A string representation of the minimum distance and resulting path.
        """

        return f"min distance: {self.min_distance}\tpath: {self.path}"

    def _dfs(self, node, visited, path) -> tuple[int, List[int]]:
        """Depth-First Search algorithm to find the shortest path in the TSP.

        Parameters
        ----------
        node : int
            The current city being visited.
        visited : List[bool]
            A List indicating whether a city has been visited or not.
        path : List[int]
            A List representing the current path traversed.

        Returns
        -------
        tuple: [int, List[int]]
            The minimum distance found and the corresponding shortest path.
        """

        visited[node] = True
        path.append(node)

        if len(path) == len(self.distance_matrix):
            return self.distance_matrix[node][path[0]], path

        min_distance = float("inf")
        min_path = None
        for i in range(len(self.distance_matrix)):
            if not visited[i]:
                distance, new_path = self._dfs(i, visited.copy(), path.copy())
                distance += self.distance_matrix[node][i]
                if distance < min_distance:
                    min_distance = distance
                    min_path = new_path

        return min_distance, min_path

    def solve(self, start: int = 0) -> None:
        """Solves the TSP.

        Parameters
        ----------
        start : int, optional
            The index of the starting city, by default 0.

        Returns
        -------
        None
        """

        n = len(self.distance_matrix)
        visited = [False] * n
        path = []

        distance, min_path = self._dfs(start, visited, path)
        min_path.append(start)
        self.min_distance = distance
        self.path = min_path

    @staticmethod
    def generate_random_distance_matrix(
        city_count: int = 5, min_distance: int = 0, max_distance: int = 10
    ) -> List[List[int]]:
        """Returns a random distance matrix between cities.

        Parameters
        ----------
        city_count : int, optional
            The number of cities, by default 5.
        min_distance : int, optional
            The minimum distance between cities, by default 0.
        max_distance : int, optional
            The maximum distance between cities, by default 10.

        Returns
        -------
        List[List[int]]
            A two-dimensional List representing the distance matrix.
        """

        matrix = generate_matrix(rows=city_count, cols=city_count)

        for i in range(city_count):
            for j in range(i + 1, city_count):
                distance = random.randint(min_distance, max_distance)
                matrix[i][j] = distance
                matrix[j][i] = distance
        return matrix
