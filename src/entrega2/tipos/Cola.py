'''
Created on 9 nov 2024

@author: alvar
'''
from __future__ import annotations
from typing import TypeVar, Generic, Callable, List
from abc import ABC, abstractmethod
from src.entrega2.tipos.Agregado_lineal import Agregado_lineal

if __name__ == '__main__':
    pass

E = TypeVar('E')
class Cola(Agregado_lineal):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of() -> 'Cola[E]':   
        return Cola()

    def add(self, e: E) -> None:
        self._elements.append(e)

    def pop(self) -> E:
        if len(self._elementos) > 0:
            return self._elementos.pop(0)
        else:
            raise IndexError("pop from empty queue")

    def __repr__(self) -> str:
        return f"Cola({', '.join(map(str, self._elements))})"
    
    