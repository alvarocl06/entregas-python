'''
Created on 9 nov 2024

@author: alvar
'''
from __future__ import annotations
from typing import TypeVar, Generic, List
from abc import ABC, abstractmethod
if __name__ == '__main__':
    pass

E= TypeVar('E')

from abc import ABC, abstractmethod
from typing import List

class Agregado_lineal(ABC):
    def __init__(self):
        
        self._elements: List = []

    def size(self) -> int:
        
        return len(self._elements)

    def is_empty(self) -> bool:
        
        return len(self._elements) == 0

    def elements(self) -> List:
        
        return self._elements

    @abstractmethod
    def add(self, e) -> None:
        
        pass

    def add_all(self, ls: List) -> None:
        
        for e in ls:
            self.add(e)

    def remove(self):
        
        assert len(self._elements) > 0, 'El agregado está vacío'
        return self._elements.pop(0)

    def remove_all(self) -> List:
        
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements

    
  