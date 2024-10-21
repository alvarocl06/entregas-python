'''
Created on 20 oct 2024

@author: alvar
'''

if __name__ == '__main__':
    pass
from math import factorial


def producto_consecutivos(n, k):
    resultado = 1
    for i in (0,k + 1):
        resultado *= n - i + 1
    return resultado

def producto_secuencia_geometrica(a1, r, k):
    producto = 1
    for n in range(1, k + 1):
        an = a1 * (r ** (n - 1))  
        producto *= an          
    return producto
 

def combinatorio(n, k):
    if k > n or n < 0 or k < 0:
        return 0  
    return factorial(n) // (factorial(k) * factorial(n - k))



def coeficiente_binomial(n, k):
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def S(n, k):
    suma = 0
    for i in range(k + 1):
        suma += ((-1) ** i) * coeficiente_binomial(k + 1, i + 1) * ((k - i) ** n)
    return suma / factorial(k)





def metodo_newton(f, df, a, epsilon):
    xn = a
    while abs(f(xn)) > epsilon:
        xn = xn - f(xn) / df(xn)
    return xn

def f(x):
    return 2*(x**2)

def df(x):
    return 4*x 


