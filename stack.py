from __future__ import annotations

from timeit import timeit
from typing import Any, List, Dict, Set, Type, NoReturn


class Stack():
    def __init__(self, items: List[Any] = []):
        self.items = items 

    def add(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)

s = Stack([1,2,3,4])
print(s.pop())
s.add(5)
print(s)
