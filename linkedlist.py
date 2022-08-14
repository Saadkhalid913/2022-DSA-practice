from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn

class Node():
    def __init__(self, val: Any, prev: Node, next: Node) -> NoReturn:
        self.v: Any = val
        self.n: Node = next 
        self.p: Node = prev 


class LinkedList():
    def __init__(self, values: List[Any]):
        self._root: Node = None
        for val in values:
            self._insert(val)

    def __repr__(self) -> str:
        vals = []
        if not self._root:
            return str(vals)

        current = self._root
        next = self._root.n
        while (next != None):
            vals.append(current.v)
            current = next 
            next = current.n
        vals.append(current.v)

        return str(vals) 
    
    def _insert(self, val: Any) -> NoReturn:
        if not self._root:
            self._root = Node(val, None, None)
        else:
            current = self._root
            next = self._root.n
            while (next != None):
                current = next 
                next = current.n
            current.n = Node(val, current, None)

    def addFirst(self, val: Any) -> NoReturn:
        newRoot = Node(val, None, self._root)
        self._root.p = newRoot
        self._root = newRoot

    def append(self, val: Any) -> NoReturn:
        self._insert(val)

    def removeFirst(self) -> Any:
        if not self._root:
            raise Exception("List is empty")
        removed = self._root
        self._root = removed.n
        return removed.v

    def removeLast(self) -> Any:
        if not self._root:      
            raise Exception("List is empty")
        current = self._root 
        next = self._root.n
        while (next != None):
            current = next 
            next = current.n
        if not current.p:
            self._root = None 
        else:
            current.p.n = None 
        val = current.v
        return val

    def getLast(self) -> Any:
        if not self._root:      
            return None 
        current = self._root 
        next = self._root.n
        while (next != None):
            current = next 
            next = current.n
        return current.v
    
    def getFirst(self) -> Any:
        if not self._root:
            return None
        else:
            return self._root.v



    
L = LinkedList([1,2,3,4])
