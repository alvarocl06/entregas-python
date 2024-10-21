'''
Created on 20 oct 2024

@author: alvar
'''
import csv
from typing import Optional

if __name__ == '__main__':
    pass


def contar(fichero, sep:str, cad:str)-> int: 
    with open(fichero, mode='r', encoding='UTF-8') as f:
        lector=f.read()
        lector=lector.lower()
        cad=cad.lower()
        divisor=lector.split(sep)
        contador=divisor.count(cad)
    return(contador)



def buscar_en_fichero(fichero, cad:str)->list[str]:
    resultado=[]
    with open(fichero, mode= 'r',encoding='utf-8') as f:
        for linea in f:
            if cad.lower() in linea.lower():
                resultado.append(linea.strip())
    return (resultado)
    


def encontrar_palabras_unicas(nombre_fichero):
    palabras_unicas = set()  
    
    try:
        with open(nombre_fichero, 'r', encoding='utf-8') as f:
            for linea in f:
               
                palabras = linea.split()  
                palabras_unicas.update(palabras)  
        
    except FileNotFoundError:
        print(f"El archivo '{nombre_fichero}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

    return list(palabras_unicas)  


from typing import Optional

def longitud_promedio_lineas(file_path,sep:str=',')-> Optional[float]:
    n=0
    terminos=0
    with open(file_path,encoding='utf-8') as f:
        lectorCSV=csv.reader(f,delimiter=sep)
        for lineas in lectorCSV:
            terminos += len(lineas)
            n+=1
    if n==0:
        return None
    
    promedio= terminos/n
    
    return promedio


file_path = 'C:/Users/alvar/git/entregas-python/resources/palabras_random.csv' 


