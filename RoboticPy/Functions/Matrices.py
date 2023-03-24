import sympy as sp
from sympy import Quaternion
from Functions.Quaternions import esta_normalizado


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

# Notas programa----------------------------#
#
# - Siendo dos matrices homogéneas T y R, siendo T una identidad + traslación y R una de rotación y vector (0,0,0), se da que RT = TR

def m_basica(eje_giro: str, angulo):
   'Crea matrices de rotación básica'
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

def m_T (eje: str, distancia):
   'Devuelve una matriz homogénea de traslación con el vector dado'
   
   iden = sp.eye(3)

   match eje:

      case 'x':
         vector = [distancia, 0, 0]
         return m_homogenea(iden, vector)
      case 'y':
            vector = [0, distancia, 0]
            return m_homogenea(iden, vector)
      case 'z':
            vector = [0, 0, distancia]
            return m_homogenea(iden, vector)

def m_Rot (eje :str, angulo):
   'Devuelve una matriz homogénea de rotación dado el ángulo y el eje de giro'

   return m_homogenea(m_basica(eje, angulo), zero)

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
      print(matriz.row(i))
      print('\n')
      print('------------------------------------')

def Cuat_a_mat(c: Quaternion) -> sp.Matrix:
   'Convierte un cuaternio en una matiz de rotación'

   esta_normalizado(c)

   nx = -(c.c)**2 -(c.d)**2 +1/2

   ox = (c.b) * (c.c) - (c.d)*(c.a)

   ax = (c.b) * (c.d) + (c.c) * (c.a)

   ny = (c.b) * (c.c) + (c.d) * (c.a)

   oy = -(c.b)**2 - (c.d)**2 +1/2

   ay = (c.c)*(c.d) - (c.b)*(c.a)

   nz = (c.b) * (c.d) - (c.c) * (c.a)

   oz = (c.c)*(c.d) + (c.b)*(c.a)

   az = -(c.b)**2 - (c.c)**2 + 1/2

   return 2 * sp.Matrix([[nx, ox, ax],
                     [ny, oy, ay],
                     [nz, oz, az]])

def Mat_a_cuat (matriz: sp.Matrix) -> Quaternion:
   'Convierte una matriz de rotación en un cuaternio'
   nx = matriz[0,0]
   ox = matriz[0,1]
   ax = matriz[0,2]

   ny = matriz[1,0]
   oy = matriz[1,1]
   ay = matriz[1,2]

   nz = matriz[2,0]
   oz = matriz[2,1]
   az = matriz[2,2]

   if (sp.sqrt(nx+oy+az+1)/2) == 0:
      print('\n', 'El primer parámetro del cuaternio es igual a 0!!!!', '\n')

   q0 = (sp.sqrt(nx+oy+az+1)/2)
   q1 = (sp.sqrt(nx-oy-az+1)/2)
   q2 = (sp.sqrt(oy-nx-az+1)/2)
   q3 = (sp.sqrt(az-nx-oy+1)/2)

   if oz-ay < 0:
      q1 = -q1
   if ax-nz < 0:
      q2 = -q2
   if ny-ox < 0:
      q3 = -q3
      
   cuaternio= Quaternion(q0, q1, q2, q3)

   return cuaternio

def extrae_Rot_Vector (m: sp.Matrix):
   'Extrae la matriz de rotación de una matriz homogénea'
   if sp.shape(m) == (4, 4):
      matriz = sp.Matrix([[m[0,0], m[0,1], m[0,2]],
                          [m[1,0], m[1,1], m[1,2]],
                          [m[2,0], m[2,1], m[2,2]]])
      
      vector = [m[0,3], m[1,3], m[2,3]]
      return matriz, vector
   else:
      print('SOLO MATRICES 4x4 HOMOGÉNEAS')


