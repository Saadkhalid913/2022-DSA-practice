from __future__ import annotations

from timeit import timeit
from typing import Any, List, Dict, Set, Type, NoReturn


class Queue():
    def __init__(self, items: List[Any] = []):
        self.items = items 

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

    def __repr__(self):
        return str(self.items)
    def __contains__(self, x):
        return x in self.items


s = Queue([1,2,3,4])
print(s.remove())
s.add(5)
print(s)