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

E = TypeVar ('E')
R = TypeVar ('R')
class Lista_ordenada_sin_repeticion(Agregado_lineal):
    def __init__(self, order: Callable[[E], R]):
        super().__init__()
        self._order = order  

    @staticmethod
    def of(order: Callable[[E], R]) -> 'Lista_ordenada_sin_repeticion':
        return Lista_ordenada_sin_repeticion(order)

    def __index_order(self, e: E) -> int:
        low, high = 0, len(self._elements)
        
        
        while low < high:
            mid = (low + high) // 2
            if self._order(self._elements[mid]) < self._order(e):
                low = mid + 1
            else:
                high = mid
        
        return low

    def add(self, e: E) -> None:
        index = self.__index_order(e)
        
        
        if index < len(self._elements) and self._order(self._elements[index]) == self._order(e):
            return  
        
        
        self._elements.insert(index, e)

    def __repr__(self):
        return f"ListaOrdenadaSinRepeticion({', '.join(map(str, self._elements))})"
    