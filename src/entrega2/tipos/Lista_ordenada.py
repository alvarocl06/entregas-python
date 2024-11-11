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
R = TypeVar('R')
      
class Lista_ordenada(Agregado_lineal, Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order

    @property
    def order(self) -> Callable[[E], R]:
        return self._order

    
    @staticmethod
    def of(order: Callable[[E], R]) -> 'ListaOrdenada[E, R]':
        return Lista_ordenada(order)

    
    def __index_order(self, e: E) -> int:
        for index, current in enumerate(self._elements):
            if self._order(e) <= self._order(current):
                return index
        return len(self._elements)

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        self._elements.insert(index, e)

    def __repr__(self) -> str:
        return f"ListaOrdenada({', '.join(map(str, self._elements))})"
    
    