'''
Created on 20 oct 2024

@author: alvar
'''

if __name__ == '__main__':
    pass

from lecturas.lecturas import *
print ('####################################')
print('TEST DE LA FUNCIÓN 6:')

fichero = 'C:/Users/alvar/git/entregas-python/resources/lin_quijote.txt'  
sep = ' '  
cad = 'quijote'  
print(f'El número de veces que aparece la palabra {cad} en el fichero {fichero} son: {contar(fichero,sep,cad)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 7:')

cad='quijote'
fichero='C:/Users/alvar/git/entregas-python/resources/lin_quijote.txt'
print(f'Las líneas en las que aparece la palabra {cad} en el archivo {fichero} son:{buscar_en_fichero(fichero, cad)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 8:')
fichero1= 'C:/Users/alvar/git/entregas-python/resources/archivo_palabras.txt'
print(f'Las palabras únicas en el fichero {fichero1},son:{encontrar_palabras_unicas(fichero1)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 9:')

file_path = 'C:/Users/alvar/git/entregas-python/resources/palabras_random.csv' 
print(f'La longitud promedio de las líneas del fichero {file_path} es: {longitud_promedio_lineas(file_path)}')

