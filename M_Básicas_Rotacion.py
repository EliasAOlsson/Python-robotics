import numpy
import sympy

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

def multiplicador (*matrices):

    for matriz in matrices:
        pass

    return resultado

