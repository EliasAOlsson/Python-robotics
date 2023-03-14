import numpy as np
import sympy as sym
import math as m

def es_menor (numero):
    'Devuelve el número 0 si es menor que el valor puesto, si no devuelve el mismo numero'
    
    try:
        if sym.Abs(numero) < 0.00001:
            return 0
    except ValueError:
        pass
    except TypeError:
        pass

    return numero

def matriz(datos):
    'Devuelve una matriz a partir de un array de datos'
    if datos == [0]:
        return np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
    else :
        Theta = datos[0]
        di = datos[1]
        ai = datos[2]
        alpha = datos[3]

        a00 = es_menor(sym.cos(Theta).evalf(2)) #type ignore
        a01 = es_menor(-sym.cos(alpha).evalf(2))*es_menor(sym.sin(Theta).evalf(2))
        a02 = es_menor(sym.sin(alpha).evalf(2))*es_menor(sym.sin(Theta).evalf(2))
        a03 = es_menor(ai)*es_menor(sym.cos(Theta).evalf(2))

        a10 = es_menor(sym.sin(Theta).evalf(2))
        a11 = es_menor(sym.cos(alpha).evalf(2))*es_menor(sym.cos(Theta).evalf(2))
        a12 = es_menor(-sym.sin(alpha).evalf(2))*es_menor(sym.cos(Theta).evalf(2))
        a13 = es_menor(ai)*es_menor(sym.sin(Theta).evalf(2))

        a21 = es_menor(sym.sin(alpha).evalf(2))
        a22 = es_menor(sym.cos(alpha).evalf(2))

        resultado = np.array([[ a00, a01 , a02 , a03 ],
                            [a10, a11 , a12 , a13],
                            [0, a21 , a22 , di],
                            [0, 0, 0, 1]])

        return resultado

#Valores simbólicos
l1 , l2, l3, l4, l5, l6, l7 = sym.symbols('l1 l2 l3 l4 l5 l6 l7')
Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sym.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sym.symbols('d1 d2 d3 d4 d5 d6 d7')

# IMPORTATE, APLICA LOS GRADOS EN RADIANES

# IMPORTANTE, .__round__ para numpy // .evalf para sympy

Datos = [[np.pi , l1, 0, np.pi/2], #Fila articulación 1
        [np.pi/2, 0, 0, -np.pi/2],
        [np.pi/2, -1, l2, -np.pi/2],
        [0, 1, 0, -np.pi/2],
        [-np.pi, l3, 0, -np.pi/2],
        [0, l4, 0, 0]]

#--------------------------------------------------------------#

'''Theta = 0
di = l4
ai = 0
alpha = 0

a00 = es_menor(sym.cos(Theta).evalf(2))
a01 = es_menor(-sym.cos(alpha).evalf(2))*es_menor(sym.sin(Theta).evalf(2))
a02 = es_menor(sym.sin(alpha).evalf(2))*es_menor(sym.sin(Theta).evalf(2))
a03 = es_menor(ai)*es_menor(sym.cos(Theta).evalf(2))

a10 = es_menor(sym.sin(Theta).evalf(2))
a11 = es_menor(sym.cos(alpha).evalf(2))*es_menor(sym.cos(Theta).evalf(2))
a12 = es_menor(-sym.sin(alpha).evalf(2))*es_menor(sym.cos(Theta).evalf(2))
a13 = es_menor(ai)*es_menor(sym.sin(Theta).evalf(2))

a21 = es_menor(sym.sin(alpha).evalf(2))
a22 = es_menor(sym.cos(alpha).evalf(2))

resultado = np.array([[ a00, a01 , a02 , a03 ],
                            [a10, a11 , a12 , a13],
                            [0, a21 , a22 , di],
                            [0, 0, 0, 1]])


Iden = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])'''

Matrices = []

Multi = matriz([0])

for articulacion in Datos:
    Matrices.append(matriz(articulacion))

for elemento in Matrices:
    Multi = Multi @ elemento

#------------------------Impresión final-----------------------------#
print()
for matriz_i in Matrices:
    print(matriz_i)
    print('---------------------------------------')
    print('\n')

for linea in Multi:
    print(linea)
    print('-')


