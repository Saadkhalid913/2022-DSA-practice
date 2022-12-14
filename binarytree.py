from __future__ import annotations
import random
from timeit import timeit
from typing import Any, List, Dict, Set, Type, NoReturn, Union
from xmlrpc.client import Boolean


class Node():
    def __init__(self, v: Any, l: Node, r: Node):
        self.v: Any = v
        self.l = l
        self.r = r 



class Tree():

    def __init__(self):
        self._root: Node = None

    def add(self, x):
        if not self._root:
            self._root = Node(x, None, None)
        else:
            self._insert(self._root, x)

    def _insert(self, node: Node, value: Any):
        if value > node.v:
            if node.r is None:
                node.r = Node(value, None, None)
            else:
                self._insert(node.r, value)
        else:
            if node.l is None:
                node.l = Node(value, None, None)
            else:
                self._insert(node.l, value)
    
    def DFT(self) -> List[int]:
        items = []
        
        self._dft(self._root, items)

        return items 

    def _dft(self, node: Node, items: List[int]) -> NoReturn:
        if node is None:
            return 
        else:
            items.append(node.v) 
            self._dft(node.l, items)
            self._dft(node.r, items)
    
    def getHeight(self) -> int:
        return self._getHeight(self._root)


    def _getHeight(self, node: Node):
        if node is None:
            return 0
        return 1 + max(self._getHeight(node.l), self._getHeight(node.r))
            

    
    def __contains__(self, value) -> bool:
        if self._root is None:
            return False 

        return self._find(self._root, value)

    def _find(self, node: Node, v) -> bool:
        if v > node.v:
            if node.r is not None:
                return self._find(node.r, v)
            else:
                return False
        else:
            if v == node.v:
                return True
            if v < node.v:
                if node.l is not None:
                    return self._find(node.l, v)
                else:
                    return False 
            

t = Tree()
t.add(10)
t.add(9)
t.add(8)
t.add(11)
t.add(12)
print(t.DFT())
print(t.getHeight())
# RangeInterval = 10**4
# trials = 100
# numbers = 1000

# def TestTreeLookup():
#     t = Tree()
#     for i in range(numbers):
#         t.add(random.randint(1, RangeInterval))

#     for i in range(numbers):
#         num = random.randint(1, RangeInterval)
#         test = num in t 


# def TestArrayLookup():
#     t = []
#     for i in range(numbers):
#         t.append(random.randint(1, RangeInterval))

#     for i in range(numbers):
#         num = random.randint(1, RangeInterval)
#         test = num in t 

# print(timeit(TestArrayLookup, number = trials))
# print(timeit(TestTreeLookup, number = trials))


    

