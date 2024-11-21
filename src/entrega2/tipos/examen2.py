'''
Created on 21 nov 2024

@author: alvar
'''
from __future__ import annotations
from typing import TypeVar, Callable, List, Optional
from abc import ABC, abstractmethod


if __name__ == '__main__':
    pass

class Agregado_lineal:
    def __init__(self):
        self.elementos = []

    def add(self, elementos):
        self.elementos.append(elementos)

    def remove(self):
        if len(self.elementos) == 0:
            raise IndexError("La cola está vacía.")
        return self.elementos.pop(0)

    def __str__(self):
        return str(self.elementos)
    
    def contains(self, e) -> bool:
        return e in self.elementos

    def find(self, func: Callable[[any], bool]) -> Optional[any]:
        for elemento in self.elementos:
            if func(elemento):
                return elemento
        return None  # Si no se encuentra ningún elemento

    def filter(self, func: Callable[[any], bool]) -> List[any]:
        return [elemento for elemento in self.elementos if func(elemento)]

class ColaConLimite(Agregado_lineal):
    def __init__(self, capacidad):
        super().__init__()
        self.capacidad = capacidad

    @classmethod
    def of(cls, capacidad):
        return cls(capacidad)

    def add(self, elemento):
        if self.is_full():
            raise OverflowError("La cola está llena.")
        super().add(elemento)

    def is_full(self):
        return len(self.elementos) >= self.capacidad

# Ejemplo de uso
cola = ColaConLimite.of(3)
cola.add("Tarea 1")
cola.add("Tarea 2")
cola.add("Tarea 3")

try:
    cola.add("Tarea 4")  # Debe lanzar OverflowError
except OverflowError as e:
    print(e)  # Debe imprimir: "La cola está llena."

print(cola.remove())  # Debe imprimir: 'Tarea 1'

if __name__ == '__main__':
    
    
