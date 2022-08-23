from __future__ import annotations

from timeit import timeit
from typing import Any, List, Dict, Set, Type, NoReturn
import random

rcInx = lambda x : 2 * x + 2
lcInx = lambda x : 2 * x + 1
pInx = lambda x : x // 2

class Heap():



    def __init__(self):
        self.items = []


    @staticmethod 
    def swap(i1: int, i2: int, arr: List[any]):
        t1 = arr[i1]
        arr[i1] = arr[i2]
        arr[i2] = t1 

    def insert(self, x):
        childInx = len(self.items)
        self.items.append(x)

        while (self.items[childInx] > self.items[pInx(childInx)]):
            self.swap(childInx, pInx(childInx), self.items)
            childInx = pInx(childInx)
    
    def pop(self):
        return self.items[0]

    def __len__(self):
        return len(self.items)
    def __repr__(self):
        return str(self.items)
    def __str__(self):
        return str(self.items)

