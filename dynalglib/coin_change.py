from typing import List


class Coin_Change:
    """Class Coin_Change is used to solve the Coin Change Problem.


    Attributes
    ----------

    coins : dict[]
        A dictionary in which the key is the denomination of the coin, and the value is the number of coins needed.
    denominations : List[int]
        A list of available denominations.
    count_coins: int
        A minimum possible number of used coins.


    Methods
    -------

    __str__()
        Returns a string representation of a class object.
    __getitem__()
        Returns number of used coins of specified denomination.
    solve()
        Finds the combination of coins that makes up the given amount or the closest possible amount.

    """

    def __init__(self, denominations: List[int] = [1, 2, 5, 10]) -> None:
        self.coins: dict = {}
        self.denominations: List[int] = sorted(denominations)
        self.count_coins: int = 0

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

        return "\t".join(f"{nominal}:{count}" for nominal, count in self.coins.items())

    def __getitem__(self, key) -> int:
        """Returns number of used coins of specified denomination.

        Parameters
        ----------
        key: int
            A specified denomination.

        Returns
        -------
        int
            A number of used coins of specified denomination.
        """

        return self.coins.get(key, 0)

    def solve(self, amount) -> None:
        """
        Finds the combination of coins that makes up the given amount or the closest possible amount.
        If it's not possible to make up the exact amount with the given denominations,
        the method stores the combination that makes up the closest possible amount in the 'result' attribute.

        Parameters
        ----------
        amount: int
            An amount for which to find the coin combination.

        Returns
        -------
        None
        """

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in self.denominations:
                if coin <= i and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1

        closest_amount = amount
        while dp[closest_amount] == float("inf"):
            closest_amount -= 1

        coins_used = {coin: 0 for coin in self.denominations}
        remaining_amount = closest_amount
        for coin in reversed(self.denominations):
            while remaining_amount >= coin:
                coins_used[coin] += 1
                remaining_amount -= coin

        self.coins = coins_used
        self.count_coins = sum(list(self.coins.values()))
