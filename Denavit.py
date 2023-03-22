import numpy as np
import sympy as sp
from sympy import pprint
from Utilities import multiplicador
from sympy import pi


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

l1 , l2, l3, l4, l5, l6, l7, l12 = sp.symbols('l1 l2 l3 l4 l5 l6 l7 l12')
Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')
a = sp.symbols('a')

I = sp.symbols('I')

#---------------------------------------------------------------#

# IMPORTATE, APLICA LOS GRADOS EN RADIANES

Datos = [[pi/2+pi, l12, -a, -pi/2],
        [0, 0, -l3, pi],
        [0, 0, l4, 0],
        [pi/2, 0, 0, -pi/2], 
        [pi/2, l5, 0, 0]]¡


#--------------------------------------------------------------#

Matrices = []

Multi = sp.eye(4)

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




