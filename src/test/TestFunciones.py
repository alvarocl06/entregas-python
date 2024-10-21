'''
Created on 20 oct 2024

@author: alvar
'''

if __name__ == '__main__':
    pass

from funciones.funciones import *

print ('####################################')
print('TEST DE LA FUNCIÓN 1:')

n=4
k=2
print(f'El producto de {n} y {k} es: {producto_consecutivos(n,k)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 2:')

a1 = 3  
r = 5
k = 2
print(f'El producto de la secuencia geométrica con a1={a1},r={r} y k={k} es: {producto_secuencia_geometrica(a1,r,k)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 3:')

n = 4
k = 2
print(f'El número combinatorio de {n} y {k} es: {combinatorio(n, k)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 4:')

n = 4
k = 2
resultado = S(n, k)
print(f'El número S(n,k) siendo n= {n} y k= {k} es: {S(n,k)}')

print ('####################################')
print('TEST DE LA FUNCIÓN 5:')

a = 3.0  
epsilon = 0.001
print(f'EL resultado de la función con a= {a} y e= {epsilon}, f(x)= 2*(x**2) y f"(x)= 4x es: { metodo_newton(f, df, a, epsilon)}')
