from __future__ import annotations

from timeit import timeit
from typing import Any, List, Dict, Set, Type, NoReturn
import random


rc = lambda x : x * 2 + 2
lc = lambda x : x * 2 + 1
pr = lambda x : (x - 1) // 2 
class Heap():
    def __init__(self):
        self.n = 0
        self.items = []

    def __len__(self):
        return self.n
    def __repr__(self):
        return str(self.items)
    def __str__(self):
        return str(self.items)
    def __getitem__(self, index):
        return self.items[index]
    def swap(self, a: int,b: int):
        tmp = self.items[b]
        self.items[b] = self.items[a]
        self.items[a] = tmp
    def rc(self, i):
        if rc(i) >= len(self):
            return None
        return self[rc(i)]
    def lc(self, i):
        if lc(i) >= len(self):
            return None
        return self[lc(i)] 

    def pr(self, i):
        if i == 0:
            return None 
        return self[pr(i)]
    def isValidParent(self, i):
        if self.lc(i) is None:
            return True 
        
        isValid = self[i] >= self.lc(i)
        if self.rc(i) is not None:
            isValid = isValid and self[i] >= self.rc(i)
        return isValid
    def largestChild(self, i):
        if self.lc(i) is None:
            return lc(i)
        if self.rc(i) is None:
            return lc(i)
        if self.lc(i) > self.rc(i):
            return lc(i)
        return rc(i)

    def insert(self, x):
        idx = len(self)
        self.items.append(x)
        self.n +=1 

        while (self[idx] > self[pr(idx)]):
            if pr(idx) < 0:
                break
            self.swap(idx, pr(idx))
            idx = pr(idx)

    def pop(self):
        if len(self) == 0:
            return None 

        maxElem = self.items[0]
        self.items[0] = self.items[-1]

        Idx = 0

        while (not self.isValidParent(Idx)):
            largestChild = self.largestChild(Idx)
            self.swap(Idx, largestChild)
            Idx = largestChild
        
        self.items.pop(-1)
        self.n -=1 
        return maxElem

def IsValid(heap : Heap):
    ind = []
    for i in range(1, len(heap)):
        ind.append(heap[i] < heap[pr(i)])
    
    return all(ind)

h = Heap()
n = 10000

a = []
b = []
for i in range(n):
    h.insert(random.randint(1, n))
    a.append(i)
for i in range(n):
    b.append(h.pop())


def isDescSorted(arr):
    length = len(arr)
    for i in range(0, length - 1):
        if arr[i] < arr[i + 1]:
            return False 
    return True 

print(isDescSorted(b))


        

