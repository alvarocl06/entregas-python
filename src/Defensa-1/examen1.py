'''
Created on 24 oct 2024

@author: alvar
'''
from math import  factorial
from math import comb
from collections import Counter
if __name__ == '__main__':
    pass

def P2(n:int,k:int,i:int= 1) -> int:
    assert n>0, 'n debe ser mayor que 0'
    assert k>0, 'k debe ser mayor que 0'
    assert i>0, 'i debe ser mayor que 0'
    assert n>=k, 'n debe ser mayor o igual a k'
    assert i<k+1, 'i debe ser menor que k + 1'
    producto=1
    for j in range(i,k + 1): 
        producto *= (n - j + 1)
    return producto

    
def C2(n: int, k: int) -> int:
    assert n>0, 'n debe ser mayor que 0'
    assert k>0, 'k debe ser mayor que 0'
    assert n>k, 'n debe ser mayor que k'
    numerador=factorial(n)
    denominador=factorial(k+1)*factorial(n-(k+1))
    return numerador // denominador

    
def S2(n: int, k: int) -> float:
    assert n>0, 'n debe ser mayor que 0'
    assert k>0, 'k debe ser mayor que 0'
    assert n>=k, 'n debe ser mayor o igual que k'
    i=0
    sumatorio=0
    for i in range(i,k+1):
        sumatorio += ((-1)**i) *comb(k,i) * (k-i)**(n+1)
        resultado= factorial(k) / (n*factorial(k+2)) * sumatorio
    return resultado


def palabrasMasComunes(fichero:str, n:int=5)-> list[tuple[str,int]]:
    assert n>1, 'n debe ser mayor que 1'
    with open (fichero,'r', encoding='UTF-8') as f:
        for linea in f:
            lector=f.read().lower()
            palabras=linea.split()
            contador=Counter(palabras)
            mas_comunes=contador.most_common()
            
    return mas_comunes
            
            
if __name__ == '__main__':
    
    try:
        print(P2(5,4))
        print(P2(6,3,2))
        print(C2(5,3))
        print(S2(6,2))
        print(palabrasMasComunes('C:/Users/alvar/git/entregas-python/resources/archivo_palabras.txt'))
        print(palabrasMasComunes('C:/Users/alvar/git/entregas-python/resources/archivo_palabras.txt',6))
    
    except ValueError as e:
        print(e)
    except AssertionError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)
    
