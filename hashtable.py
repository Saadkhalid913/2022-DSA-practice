from __future__ import annotations

from timeit import timeit
from typing import Any, List, Dict, Set, Type, NoReturn
import sys 

class Hashtable():
    def __init__(self, length: int):
        self.length: int = length 
        self.items: List[List] = [False] * self.length
        self.keys = []

    def __getitem__(self, key):
        if key not in self.keys:
            raise KeyError("Key does not exist")

        hashed_key = id(key) % (self.length)
        
        i = 1
        while not self.items[hashed_key][0] == key:
            hashed_key = (hashed_key + i ** 2) % (self.length)
        return self.items[hashed_key][1]

    def __setitem__(self, key, value):
        if (key in self.keys):
            raise KeyError("Key already exists")

        hashed_key = id(key) % (self.length)
        if not self.items[hashed_key]:
            self.items[hashed_key] = (key, value)
            self.keys.append(key)
        else:
            i = 1
            while self.items[hashed_key] != False:
                hashed_key = (hashed_key + i ** 2) % (self.length)
            self.items[hashed_key] = (key, value)



    def __repr__(self) -> str:
        repr = "{"
        for key, value in self.items:
            repr = repr + f"{str(key)}: {str(value)},"

        repr = repr + "}"
        return repr 
        
    def __str__(self) -> str:
        repr = "{"
        for key,value in self.items:
                repr = repr + f"\n {str(key)}: {str(value)},"

        repr = repr + "\n}"
        return repr 

if __name__ == "__main__":
    H = Hashtable(10)
    H[1] = "hello"
    print(H[1])

