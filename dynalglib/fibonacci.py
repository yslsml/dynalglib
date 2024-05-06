class Fibonacci:
    """Class Fibonacci is used to calculate a series of Fibonacci numbers.


    Attributes
    ----------

    _cache : List[int]
        A list of already calculated Fibonacci numbers.


    Methods
    -------

    __str__()
        Returns a string representation of a class object.
    __getitem__()
        Returns item by its index.
    __extend_cache()
        Is used to extend cache list of Fibonacci numbers up to given index.


    Example
    -------

    >>> from dynalglib import Fibonacci
    >>> fibonacci = Fibonacci()
    >>> print(fibonacci[5]) # prints 5th Fibonacci number

    """

    def __init__(self) -> None:
        self._cache = [0, 1]

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

        return str(self._cache)

    def __getitem__(self, key) -> int:
        """Returns item by its index.

        Parameters
        ----------
        key : int
            An index of the desired element.

        Returns
        -------
        int
            A desired element.

        Raises
        ------
        ValueError
            If given parameter key is negative.
        """

        if key < 0:
            raise ValueError("Index must be non-negative")

        if key >= len(self._cache):
            self.__extend_cache(key)
        return self._cache[key]

    def __extend_cache(self, n) -> None:
        """Is used to extend cache list of Fibonacci numbers up to given index.

        Parameters
        ----------
        n : int
            An index of the element up to which the cache will be extended.

        Returns
        -------
        None
        """

        for i in range(len(self._cache), n + 1):
            self._cache.append(self._cache[i - 1] + self._cache[i - 2])
