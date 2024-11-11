'''
Created on 9 nov 2024

@author: alvar
'''

if __name__ == '__main__':
    pass

from src.entrega2.tipos.Cola_prioridad import *
def test_cola_prioridad():
    cola = ColaDePrioridad[str, int]()
    # Agregar pacientes
    cola.add('Paciente A', 3) # Dolor de cabeza leve
    cola.add('Paciente B', 2) # Fractura en la pierna
    cola.add('Paciente C', 1) # Ataque cardíaco
    
    assert cola.elements() == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de la cola es incorrecto."
    atencion = []
    while not cola.is_empty():
        atencion.append(cola.remove())

    assert atencion == ['Paciente C', 'Paciente B', 'Paciente A'], "El orden de atención no es correcto."
    print("Pruebas superadas exitosamente.")
if __name__ == '__main__':
    test_cola_prioridad()