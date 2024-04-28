import pytest
from dynalglib import Fibonacci


@pytest.mark.parametrize(
    "index, value",
    [(10, 55), (25, 75025), (60, 1548008755920), (100, 354224848179261915075)],
)
def test_fibonacci(index, value):
    fib = Fibonacci()
    assert fib[index] == value
