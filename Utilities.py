import sympy as sp
import numpy as np

'''
Algunos comandos útiles:
    matrix_a.dot(matrix_b) -> Producto escalar

    matrix_a.cross(matrix_b) -> Producto vectorial

'''

def es_menor (numero):
    'Devuelve el número 0 si es menor que el valor puesto, si no devuelve el mismo numero'
    
    try:
        if sp.Abs(numero) < 0.0001:
            return 0
    except ValueError:
        pass
    except TypeError:
        pass

    return numero

def multiplicador (tamaño: int, post_or_pre: str, matrices: list):
    '''Multiplica las matrices introducidas en una lista y devuelve el resultado.
    Importante el argumento Post -> Móviles // Pre -> Fijos'''

    resultado = sp.eye(tamaño)

    if post_or_pre == 'pre':

        for matriz in matrices:
            resultado = matriz @ resultado
            resultado.simplify()

    elif post_or_pre == 'post':
        for matriz in matrices:
            resultado = resultado @ matriz
            resultado.simplify()
    else:
        print("Introduce 'post' o 'pre'.")

    return resultado

def rad(angulo: float):
    'Devuelve el ángulo introducido convertido a radianes'
    return angulo*(np.pi/180)


'''v1 = sp.Matrix([[0.6427, 0.616, 0.4562]])
v2 = sp.Matrix([[0.4275, -0.7815, 0.4544]])

v3 = v2.cross(v1)

sp.pprint(v3)'''