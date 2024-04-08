# dynalglib   

<p style="text-align:center">
<a href="https://github.com/yslsml/dynalglib/actions/workflows/tests.yaml"><img alt="Actions Status" src="https://github.com/yslsml/dynalglib/actions/workflows/tests.yaml/badge.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

Dynalglib is a library which is designed to solve some of dynamic programming algorithms in Python.


## Released algorithms:
- Knapsack problem
- Traveling Salesman Problem


## Installing

## A simple example
``` python
from dynalglib import Item
from dynalglib import Knapsack

knapsack = Knapsack(
    items=[
        Item(name="apple", weight=2, value=3, quantity=6),
        Item(name="pineapple", weight=4, value=8, quantity=3),
        Item(name="kiwi", weight=3, value=6, quantity=3),
        Item(name="strawberry", weight=1, value=7, quantity=8),
    ],
    capacity=10,
)

knapsack.fill() 
print(knapsack.total_value)
print(knapsack)
```
