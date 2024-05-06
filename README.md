# dynalglib

[![Tests](https://github.com/yslsml/dynalglib/actions/workflows/tests.yaml/badge.svg)](https://github.com/yslsml/dynalglib/actions/workflows/tests.yaml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Dynalglib is a library which is designed to solve problems using dynamic programming algorithms in Python.


## Released algorithms:
- Fibonacci
- Knapsack Problem
- Traveling Salesman Problem
- Resource Allocation Problem
- Coin Change Problem


## Installing
To install this library you should run:
``` bash
pip install dynalglib    
```
     
To update the library you should run:
``` bash 
pip install -U dynalglib
```


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
