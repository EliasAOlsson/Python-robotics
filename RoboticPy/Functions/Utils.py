import sympy as sp

def simplify_matrix(matriz):
    'Matrix "simplificator"'
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

def simply (number):
    'Returns a 0 if the argument is smaller than the specified limit. If the argument is a sympy symbolic, it just returns the simbolic.'
    
    limit = 0.0001

    try:
        if sp.Abs(number) < limit:
            return 0
    except ValueError:
        pass
    except TypeError:
        pass

    return number

def multiplicator(size: int, post_or_pre: str, matrices: list):
    ''' Multiplies the matrices in the "matrices" list and returns the sucesive result.
    It is important to specify the order of multiplication:

    Post --> The multiplication goes from left to right.

    Pre --> The multiplication goes from right to left.
    '''

    result = sp.eye(size)

    if post_or_pre == 'pre':

        for matrix in matrices:
            result = matrix @ result
            result.simplify()

    elif post_or_pre == 'post':
        for matrix in matrices:
            result = result @ matrix
            result.simplify()
    else:
        print("Introduce 'post' o 'pre'.")

    return simplify_matrix(result)

def rad(angle: float):
    'Returns the angle specified as argument to radians' 
    return (angle*(sp.pi/180)).evalf(5)


