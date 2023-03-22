import sympy
from sympy import Matrix


a = Matrix([1,0,0])
b = Matrix([0,2,0])

print(b.cross(a))