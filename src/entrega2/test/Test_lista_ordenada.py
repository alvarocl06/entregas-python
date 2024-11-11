'''
Created on 9 nov 2024

@author: alvar
'''
from src.entrega2.tipos.Lista_ordenada import Lista_ordenada

lista = Lista_ordenada.of(lambda x: x)
lista.add(3)
lista.add(1)
lista.add(2)

print (f'resultado de la lista: {lista}')

print(f'el elemento eliminado al utilizar remove(): {lista.remove()}')
lista.add(1)

print(f'elementos eliminados al utilizar remove_all(): {lista.remove_all()}')

lista.add(3)
lista.add(1)
lista.add(2)
lista.add(0)
print(f'lista después de añadir el 0: {lista}')
lista.add(10)
print(f'lista después de añadir el 10: {lista}')
lista.add(7)
print(f'lista después de añadir el 7: {lista}')