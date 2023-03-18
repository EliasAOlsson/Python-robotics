import numpy as np
import sympy as sp
from sympy import pprint
from Utilities import multiplicador

'''
NOTAS

# print(matriz_i[0][0]) -> Operador acceso a arrays de N dimensiones

# print(Multi[0,3]) -> Operador acceso a matrices

'''

def matriz(datos):
    'Devuelve una matriz a partir de un array de datos'
    if datos == [0]:
        return sp.Matrix([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
    else :
        Theta = datos[0]
        di = datos[1]
        ai = datos[2]
        alpha = datos[3]

        ''' a00 = es_menor(sp.cos(Theta)) #type ignore
        a01 = es_menor(-sp.cos(alpha))*es_menor(sp.sin(Theta))
        a02 = es_menor(sp.sin(alpha))*es_menor(sp.sin(Theta))
        a03 = es_menor(ai)*es_menor(sp.cos(Theta))

        a10 = es_menor(sp.sin(Theta))
        a11 = es_menor(sp.cos(alpha))*es_menor(sp.cos(Theta))
        a12 = es_menor(-sp.sin(alpha))*es_menor(sp.cos(Theta))
        a13 = es_menor(ai)*es_menor(sp.sin(Theta))

        a21 = es_menor(sp.sin(alpha))
        a22 = es_menor(sp.cos(alpha))'''

        a00 = (sp.cos(Theta)).simplify()
        a01 = (-sp.cos(alpha)*sp.sin(Theta)).simplify()
        a02 = (sp.sin(alpha)*sp.sin(Theta)).simplify()
        a03 = (ai*sp.cos(Theta)).simplify()

        a10 = (sp.sin(Theta)).simplify()
        a11 = (sp.cos(alpha)*sp.cos(Theta)).simplify()
        a12 = (-sp.sin(alpha)*sp.cos(Theta)).simplify()
        a13 = (ai*sp.sin(Theta)).simplify()

        a21 = (sp.sin(alpha)).simplify()
        a22 = (sp.cos(alpha)).simplify()

        resultado = sp.Matrix([[ a00, a01 , a02 , a03 ],
                            [a10, a11 , a12 , a13],
                            [0, a21 , a22 , di],
                            [0, 0, 0, 1]])

        return resultado

# Valores simbólicos--------------------------------------------#

l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')

#---------------------------------------------------------------#

# IMPORTATE, APLICA LOS GRADOS EN RADIANES

'''Datos = [[sp.pi , l1, 0, sp.pi/2], #Fila articulación 1
        [sp.pi/2, 0, 0, -sp.pi/2],
        [sp.pi/2, -1, l2, -sp.pi/2],
        [0, 1, 0, -sp.pi/2],
        [-sp.pi, l3, 0, -sp.pi/2],
        [0, l4, 0, 0]]'''

'''Datos = [[Theta_1 , l1+l2, 0, sp.pi], 
        [-sp.pi/2, d2, 0, sp.pi/2],
        [0, d3-l3, 0, sp.pi],
        [Theta_4, l4, 0, 0]]'''

Datos = [[Theta_1+(sp.pi/2) , 2.25, 0, (sp.pi/6)+(sp.pi/2)], #Fila articulación 1
        [0, d2, 0, -sp.pi/2],
        [Theta_3, l3, 0, 0]]


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

Multi = sp.eye(4) #

for articulacion in Datos:
    Matrices.append(matriz(articulacion))

Multi = multiplicador(4, 'post', Matrices)

Multi.simplify() #Ojo con el simplify

#------------------------Impresión final-----------------------------#
print()
for matriz_i in Matrices:
    
    pprint(matriz_i)
    print('---------------------------------------', '\n')

pprint(Multi)




