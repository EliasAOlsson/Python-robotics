import sympy as sp

'''
Algunos comandos útiles:
    matrix_a.dot(matrix_b) -> Producto escalar

    matrix_a.cross(matrix_b) -> Producto vectorial
'''

def simplifica_matriz(matriz):
    'Metodo para simplificar matrices'
    'Créditos a Alvaro Navarro Jorquera'
    for i in range(len(matriz)):
        matriz[i] = matriz[i].evalf(4)
        try:
            matriz[i] = round(matriz[i],4)
        except TypeError:
            for a in sp.preorder_traversal(matriz[i]):
                if isinstance(a, sp.Float):
                    matriz[i] = matriz[i].subs(a, round(a,4))   
    return matriz

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

def multiplicador(tamaño: int, post_or_pre: str, matrices: list):
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

    return simplifica_matriz(resultado)

def rad(angulo: float):
    'Devuelve el ángulo introducido convertido a radianes'
    return (angulo*(sp.pi/180)).evalf(5)


