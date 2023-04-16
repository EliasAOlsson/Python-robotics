import sympy as sp
from sympy import Quaternion
from Functions.Quaternions import is_normalized


def m_basic(rotation_axis: str, angle):
   'Returns a basic rotation matrix around the specified rotation axis and angle.'
   match rotation_axis:

      case 'x':
         return sp.Matrix([[1, 0, 0],
                          [0, sp.cos(angle),-sp.sin(angle)],
                          [0, sp.sin(angle), sp.cos(angle)]])
      case 'y':
         return sp.Matrix([[sp.cos(angle), 0, sp.sin(angle)],
                          [0, 1, 0],
                          [-sp.sin(angle), 0, sp.cos(angle)]])
      case 'z':
         return sp.Matrix([[sp.cos(angle), -sp.sin(angle), 0],
                          [sp.sin(angle), sp.cos(angle), 0],
                          [0, 0, 1]])

def m_T (axis: str, distance):

   'Returns a homogeneus rotation matrix with the specified axis and distance (Only one axis). [No rotation]'
   
   iden = sp.eye(3)

   match axis:

      case 'x':
         vector = [distance, 0, 0]
         return m_homo(iden, vector)
      case 'y':
            vector = [0, distance, 0]
            return m_homo(iden, vector)
      case 'z':
            vector = [0, 0, distance]
            return m_homo(iden, vector)

def m_Rot (eje :str, angulo):
   'Returns a homogeneous rotation matrix with the specified angle and rotation axis (Only one axis). [No movement]'

   zero = [0, 0, 0]

   return m_homo(m_basic(eje, angulo), zero)

def m_homo(matriz_rot, vector: list):
   'Returns a homogeneous transformation matrix with the specified rotation matrix and movement vector'
   
   vector_p = sp.Matrix([vector[0], vector[1], vector[2]])
   if not isinstance(matriz_rot, sp.Matrix):
      matriz_rot = matriz_rot.tomatrix()

   matriz_rot = matriz_rot.col_insert(4, vector_p)
   matriz_rot = matriz_rot.row_insert(4, sp.Matrix([[0,0,0, 1]]))
   
   return matriz_rot

def m_print(matriz: sp.Matrix)-> None:

   'Function that prints a matrix, with each row separated by a line. Useful for big matrices'

   print('M_print OUTPUT: ', '\n')
   tam = sp.shape(matriz)
   for i in range(tam[0]):
      print(matriz.row(i))
      print('\n')
      print('------------------------------------')

def Cuat_a_mat(c: Quaternion) -> sp.Matrix:
   'Converts a quaternion into a rotation matrix'

   is_normalized(c)

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

   'Converts a rotation matrix into a quaternion'

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
      print('\n', 'Q0 is equal to 0!!!!', '\n')

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
      
   cuaternion= Quaternion(q0, q1, q2, q3)

   return cuaternion

def extract_rot_vector (m: sp.Matrix):

   'Extracts the basic rotation matrix and movement vector from an homogeneous transformation matrix.'

   if sp.shape(m) == (4, 4):
      matrix = sp.Matrix([[m[0,0], m[0,1], m[0,2]],
                          [m[1,0], m[1,1], m[1,2]],
                          [m[2,0], m[2,1], m[2,2]]])
      
      vector = [m[0,3], m[1,3], m[2,3]]
      return matrix, vector
   else:
      print('Only homogeneous tranformation matrices (4x4)')


