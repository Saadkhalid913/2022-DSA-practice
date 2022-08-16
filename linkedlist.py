from __future__ import annotations
from typing import Any, List, Dict, Set, Type, NoReturn
from timeit import timeit
import random
class Node():
    def __init__(self, val: Any, prev: Node, next: Node) -> NoReturn:
        self.v: Any = val
        self.n: Node = next 
        self.p: Node = prev 


class LinkedList():
    '''
        Doubly Linked List implementation
    
    '''
    def __init__(self, values: List[Any]):
        self._root: Node = None
        self.length: int = 0
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

    def __len__(self) -> int:
        return self.length
            
    
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
        self.length +=1 

    def addFirst(self, val: Any) -> NoReturn:
        newRoot = Node(val, None, self._root)
        self._root.p = newRoot
        self._root = newRoot
        self.length +=1 

    def append(self, val: Any) -> NoReturn:
        self._insert(val)

    def removeFirst(self) -> Any:
        if not self._root:
            raise Exception("List is empty")
        removed = self._root
        self._root = removed.n
        
        self.length -=1 
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
        self.length -=1 
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
            

    def insert(self, val: Any, index: int) -> NoReturn:
        if index == 0:
            self.addFirst(val)
        else:
            assert index < len(self)
            current_index = 1 
            current = self._root
            next = current.n
            while (next != None and current_index < index):
                current = next 
                next = current.n
                current_index +=1 
            
            # save old ith node 
            temp = current.n

            # add new node in front of current and make it point to the old ith node (now i + 1th node)
            current.n = Node(val, current, temp)

            self.length +=1 

    def reverse(self) -> LinkedList:
        if not self._root:
            return self 
        current = self._root 
        next = self._root.n
        self._root.n = None 
        while (next != None):
            temp = next.n
            next.n = current 
            current = next 
            next = temp 
        self._root = current 
        
        return self 

    def __getitem__(self, index):
        if not self._root or index >= len(self):
            raise IndexError("Index out of bounds")
        if index < 0:
            return self[index % len(self)]
        
        i = 0
        current = self._root
        next = self._root.n
        while i < index:
            current = next 
            next = current.n 
            i +=1 
        return current.v 

    def getKthItemFromBack(self, k):
        forwardIndex = 0
        if not self._root:
            return 

        pointer = None 
        next_pointer = None

        current = self._root 
        next = self._root.n
        while next != None:
            current = next 
            next = current.n
            if forwardIndex == ( k - 1 ):
                pointer = self._root
                next_pointer = pointer.n
            forwardIndex +=1 
            
            if (pointer != None):
                pointer = next_pointer
                next_pointer = pointer.n
            
        return pointer.v 


num_trials = 10000 ## linear 
num_items = 1000
L = LinkedList([i for i in range(1, num_items)])

def CreateList():
    L = LinkedList([i for i in range(1, num_items)])

def TestMoshMethod():
    index = random.randint(1, num_items - 2)
    kth_Item = (L.getKthItemFromBack(index))

def TestMyMethod():
    index = random.randint(1, num_items - 2)
    kth_Item = (L[-index])


print("Time to create array" ,timeit( CreateList, number = 1))
print("Time for my method", timeit(TestMyMethod, number = num_trials), "sec")



