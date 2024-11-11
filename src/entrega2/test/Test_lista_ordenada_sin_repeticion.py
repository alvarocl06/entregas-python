'''
Created on 9 nov 2024

@author: alvar
'''
from src.entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion
if __name__ == '__main__':
    pass

lista= Lista_ordenada_sin_repeticion.of(lambda x: -x)
lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)

print(f'el resultado de la lista ordenada sin repetición es: {lista}')

print(f'el elemento ekiminado al utilizar remove(): {lista.remove()}')
lista.add(47)

print(f'elementos eliminados al utilizar remove_all(): {lista.remove_all()}')

lista.add(23)
lista.add(47)
lista.add(47)
lista.add(1)
lista.add(2)
lista.add(-3)
lista.add(4)
lista.add(5)

lista.add(0)
print(f'lista después de añadir el 0 {lista}')
lista.add(0)
print(f'lista después de añadir el 0: {lista}')
lista.add(7)
print(f'lista después de añadir el 7: {lista}')
