import numpy as np
import sympy as sp
from Utilities import multiplicador
from sympy import pprint

'''
Matriz básica de rotación
   u      v      w
| n_x    o_x    a_x| x
| n_y    o_y    a_y| y
| n_z    o_z    a_z| z

Donde cada componente es coseno del ángulo del indicado
eje movil respecto del eje fijo correspondiente

n_x = coseno(alpha)

Siendo alpha el ángulo entre u y x

PROPIEDADES

El producto escalar de cada fila [n, o, a] NO debe ser
superior a 1

filas de 0 0 1 -> Posibles
filas de 0 2 0 -> NO POSIBLE -> 0 de nota

M ^-1 = M ^T (Matriz traspuesta = Inversa)

La matriz de rotación del sistema u,v,w respecto del x,y,z
es la inversa de la matriz de rot. del sistema
x,y,z respecto del u,v,w

'''

def matriz_rot(angulo, eje_giro: str):
   'Crea matrices de rotación homogénea'
   match eje_giro:

      case 'x':
         return sp.Matrix([[1, 0, 0],
                          [0, sp.cos(angulo),-sp.sin(angulo)],
                          [0, sp.sin(angulo), sp.cos(angulo)]])
      case 'y':
         return sp.Matrix([[sp.cos(angulo), 0, sp.sin(angulo)],
                          [0, 1, 0],
                          [-sp.sin(angulo), 0, sp.cos(angulo)]])
      case 'z':
         return sp.Matrix([[sp.cos(angulo), -sp.sin(angulo), 0],
                          [sp.sin(angulo), sp.cos(angulo), 0],
                          [0, 0, 1]])

def matriz_homogenea(matriz_rot, vector: list):
   
   vector_p = sp.Matrix([vector[0], vector[1], vector[2]])
   if not isinstance(matriz_rot, sp.Matrix):
      matriz_rot = matriz_rot.tomatrix()

   matriz_rot = matriz_rot.col_insert(4, vector_p)
   matriz_rot = matriz_rot.row_insert(4, sp.Matrix([[0,0,0, 1]]))
   
   pprint(matriz_rot)
   return matriz_rot

iden = sp.eye(3)
zero = [0,0,0]

m1 = matriz_homogenea(matriz_rot((sp.pi), 'x'), zero)
m2 = matriz_homogenea(iden, [1,0,0])
m3 = matriz_homogenea(matriz_rot((sp.pi), 'y'), zero)
m4 = matriz_homogenea(matriz_rot((sp.pi), 'y'), zero)
m5 = matriz_homogenea(iden, [0,0,1])

matrices = [m4, m2, m1, m3, m5]

solucion = multiplicador(4, 'pre', matrices)
pprint(solucion)