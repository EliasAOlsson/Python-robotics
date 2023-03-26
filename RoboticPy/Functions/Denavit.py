import sympy as sp
from sympy import pprint
from sympy import pi
from sympy import Matrix
from Functions.Utils import multiplicador 

# Se importa Utils sin Functions.Utils
# porque la función multiplicador se utiliza SOLO cuando este script se ejecuta como __main__


'''
NOTAS

# print(matriz_i[0][0]) -> Operador acceso a arrays de N dimensiones

# print(Multi[0,3]) -> Operador acceso a matrices

'''

def matriz_articulacion(datos:list) -> Matrix:
    'Devuelve una matriz a partir de una matrix de datos'

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

def impresion_completa(Datos:list[list]) -> None:
    'Imprime las matrices de la lista y su post-multiplicación'

    Matrices = []
    Multi = sp.eye(4)

    for articulacion in Datos:
        Matrices.append(matriz_articulacion(articulacion))

    Multi = multiplicador(4, 'post', Matrices)

    Multi.simplify()

    #------------------------Impresión final-----------------------------#
    print()
    for matriz_i in Matrices:

        pprint(matriz_i)
        print('---------------------------------------', '\n')

    pprint(Multi)





