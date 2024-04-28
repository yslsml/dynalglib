import pytest
from dynalglib import Item
from dynalglib import Knapsack


@pytest.mark.parametrize(
    "items, capacity, expected_value",
    [
        (
            [
                Item(name="1", weight=2, value=3, quantity=6),
                Item(name="2", weight=4, value=8, quantity=3),
                Item(name="3", weight=3, value=6, quantity=3),
                Item(name="4", weight=1, value=7, quantity=8),
            ],
            10,
            59,
        ),
        (
            [
                Item(name="1", weight=2, value=11, quantity=5),
                Item(name="2", weight=4, value=24, quantity=2),
                Item(name="3", weight=8, value=42, quantity=3),
                Item(name="4", weight=1, value=5, quantity=6),
            ],
            12,
            70,
        ),
    ],
)
def test_knapsack(items, capacity, expected_value):
    knapsack = Knapsack(items=items, capacity=capacity)
    knapsack.fill()
    assert knapsack.total_value == expected_value
