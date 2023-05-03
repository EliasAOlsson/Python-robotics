import sympy as sp
from sympy import pprint
from sympy import pi
from sympy import Matrix
from Functions.Utils import multiplicator

def articulation_matrix(data:list) -> Matrix:
    'Returns a matrix from a Denavit-Hartenberg matrix'

    if data == [0]:
        return sp.Matrix([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 1]])
    else :
        Theta = data[0]
        di = data[1]
        ai = data[2]
        alpha = data[3]

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

        result = sp.Matrix([[ a00, a01 , a02 , a03 ],
                            [a10, a11 , a12 , a13],
                            [0, a21 , a22 , di],
                            [0, 0, 0, 1]])

        return result

def Complete_print(Data:list[list]) -> None:
    '''Receives as argument the complete table from Denavit-Hartenberg algorithm.
    Prints the rotation matrix asociated to each articulation AND the final post-multiplication
    of each rotation matrix (which would be the resulting rotation matrix of the whole robot)
    
    Example of code found on the documentation.'''

    Matrices = []
    Multi = sp.eye(4)

    for articulacion in Data:
        Matrices.append(articulation_matrix(articulacion))

    Multi = multiplicator(4, 'post', Matrices)

    Multi.simplify()

    #------------------------Final print-----------------------------#
    print()
    for matriz_i in Matrices:

        pprint(matriz_i)
        print('---------------------------------------', '\n')

    pprint(Multi)





