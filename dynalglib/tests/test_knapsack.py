from dynalglib import Item
from dynalglib import Knapsack


def test_first() -> None:
    knapsack = Knapsack(
        items=[
            Item(name="1", weight=2, value=3, quantity=6),
            Item(name="2", weight=4, value=8, quantity=3),
            Item(name="3", weight=3, value=6, quantity=3),
            Item(name="4", weight=1, value=7, quantity=8),
        ],
        capacity=10,
    )
    knapsack.fill()
    assert knapsack.total_value == 59


def test_two() -> None:
    knapsack = Knapsack(
        items=[
            Item(name="1", weight=2, value=11, quantity=5),
            Item(name="2", weight=4, value=24, quantity=2),
            Item(name="3", weight=8, value=42, quantity=3),
            Item(name="4", weight=1, value=5, quantity=6),
        ],
        capacity=12,
    )
    knapsack.fill()
    assert knapsack.total_value == 70
