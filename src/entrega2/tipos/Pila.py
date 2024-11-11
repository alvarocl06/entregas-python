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

class Pila(Agregado_lineal):
    def __init__(self):
        super().__init__()

    @staticmethod
    def of():
        return Pila()

    def add(self, e):
        self._elements.insert(0, e)

    def top(self):
        assert not self.is_empty(), 'La pila está vacía'
        return self._elements[0]

    def pop(self):
        assert not self.is_empty(), 'La pila está vacía'
        return self._elements.pop(0)