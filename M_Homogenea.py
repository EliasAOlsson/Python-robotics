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

def m_rot(angulo, eje_giro: str):
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

def m_homogenea(matriz_rot, vector: list):
   'Devuelve una matriz homogénea a partir de una matriz básica de rotación y su vector de movimiento'
   
   vector_p = sp.Matrix([vector[0], vector[1], vector[2]])
   if not isinstance(matriz_rot, sp.Matrix):
      matriz_rot = matriz_rot.tomatrix()

   matriz_rot = matriz_rot.col_insert(4, vector_p)
   matriz_rot = matriz_rot.row_insert(4, sp.Matrix([[0,0,0, 1]]))
   
   return matriz_rot

def m_print(matriz: sp.Matrix)-> None:
   'Función para "printear" cada línea de la matriz por separado'
   print('Salida m_print: ', '\n')
   tam = sp.shape(matriz)
   for i in range(tam[0]):
      pprint(solucion.row(i))
      print('\n')
      print('------------------------------------')

#### NOTA IMPORTANE -> Problemas con el uso de la letra R como símbolo ###

# Valores simbólicos--------------------------------------------#

l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')
Gamma_1 = sp.symbols('Gamma_1')

a1, a2 = sp.symbols('a1 a2')

iden = sp.eye(3)
zero = [0,0,0]

#---------------------------------------------------------------#

t1 = m_homogenea(iden, [0,0,l1])
r1 = m_homogenea(m_rot(Theta_1, 'z'), zero)
t2 = m_homogenea(iden, [0,a1,0])
t3 = m_homogenea(iden, [0,0,a2])
r2 = m_homogenea(m_rot((Theta_2), 'y'), zero)
r3 = m_homogenea(m_rot(-Theta_1, 'z'), zero)
t4 = m_homogenea(iden, [0,l2,0])
r4 = m_homogenea(m_rot(sp.pi/4, 'x'), zero)
t5 = m_homogenea(iden, [0,l3,0])
t6 = m_homogenea(iden, [0,0,d2])
r5 = m_homogenea(m_rot(-sp.pi/4, 'x'), zero)


matrices = [t1,r1,t2,t3,r2,r3,t4,r4,t5,t6,r5]

solucion = multiplicador(4, 'post', matrices)

solucion.simplify()

m_print(solucion)



