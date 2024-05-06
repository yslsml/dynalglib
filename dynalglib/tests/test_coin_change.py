import pytest
from dynalglib.coin_change import Coin_Change


@pytest.mark.parametrize(
    "value, count_coins", [(54, 7), (1564, 158), (7567, 758), (95724, 9574)]
)
def test_exact_match_count_coins(value, count_coins):
    coin = Coin_Change(denominations=[10, 5, 2, 1])
    coin.solve(value)
    assert coin.count_coins == count_coins


@pytest.mark.parametrize(
    "value, count_coins", [(57, 6), (1563, 157), (7565, 757), (95721, 9572)]
)
def test_nearest_match_count_coins(value, count_coins):
    coin = Coin_Change(denominations=[10, 2, 6, 4, 8])
    coin.solve(value)
    assert coin.count_coins == count_coins


@pytest.mark.parametrize(
    "value, dict_coins",
    [
        (54, {1: 0, 2: 2, 5: 0, 10: 5}),
        (1564, {1: 0, 2: 2, 5: 0, 10: 156}),
        (7567, {1: 0, 2: 1, 5: 1, 10: 756}),
        (95724, {1: 0, 2: 2, 5: 0, 10: 9572}),
    ],
)
def test_dict_coins(value, dict_coins):
    coin = Coin_Change(denominations=[10, 5, 2, 1])
    coin.solve(value)
    assert coin.coins == dict_coins
