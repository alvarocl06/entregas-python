'''
Created on 9 nov 2024

@author: alvar
'''
from src.entrega2.tipos.Cola import Cola
if __name__ == '__main__':
    pass

cola= Cola.of()
cola.add_all([23,47,1,2,-3,4,5])
print(f'resultado de la cola: {cola}')

print(f'elementos eliminados al utilizar remove_all(): {cola.remove_all()}')