import sympy as sp
import math as mt
import numpy as np
from sympy import Quaternion

def q_mul (cuaterniones:list, post_or_pre : str) -> Quaternion | None:
    'Multiplicación de cuaterniones en una lista. Post -> Móviles // Pre -> Fijos'

    if post_or_pre == 'pre':
        cuaterniones.reverse()
        resultado = cuaterniones[0]
        for cuaternion in cuaterniones:
            if cuaternion == cuaterniones[0]:
                continue
            else:
                resultado = resultado.mul(cuaternion)
        return resultado

    elif post_or_pre == 'post':
        resultado = cuaterniones[0]
        for cuaternion in cuaterniones:
            if cuaternion == cuaterniones[0]:
                continue
            else:
                resultado = resultado.mul(cuaternion)
        return resultado

    else:
        print("Introduce 'post' o 'pre'.")

def q_eje (eje: str, angulo) -> Quaternion | None:
    'Devuelve un cuaternion básico de giro sobre X, Y o Z'

    eje = eje.lower()

    match eje:

      case 'x':
            return sp.Quaternion(sp.cos(angulo/2),sp.sin(angulo/2),0,0)
      case 'y':
            return sp.Quaternion(sp.cos(angulo/2),0,sp.sin(angulo/2),0)
      case 'z':
            return sp.Quaternion(sp.cos(angulo/2),0,0,sp.sin(angulo/2))
            
def q_conj(cuaternion: Quaternion) -> Quaternion:
    'Devuelve el conjugado del cuaternio'

    return Quaternion(cuaternion.args[0], -cuaternion.args[1], -cuaternion.args[2], -cuaternion.args[3])

def qprint(cuaternion: Quaternion) -> None:
    'Printea el cuaternion y cada elemento separado por guiones'
    
    print('\n', cuaternion, '\n')
    
    for element in cuaternion.args:
        print(element)
        print('---------------------------')

def qtras_rot(cuaternio: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:
    'Devuelve el vector resultado de la operación con traslaciones y rotaciones'

    multi = [cuaternio, v , q_conj(cuaternio)]

    return q_mul(multi, 'post').add(P)

# NOTAS IMPORTANTES LEER ****
'''
 - Llamar a la función quat_eje con el ángulo SIN dividir entre 2

'''
#Cuaternio identidad = (1,0,0,0)

iden = Quaternion(1, 0, 0, 0)

# Valores simbólicos--------------------------------------------#

l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')

Alpha = sp.symbols('Alpha')

#---------------------------------------------------------------#

#IMPORTANTE -> Recuerda el uso de .simplify()


q_01p = q_mul([q_eje('x', sp.pi/2), q_eje('y', sp.pi/2+Theta_1)],'post')

q_1p1 = q_eje('x', sp.pi/6)

q_12 = q_eje('x', sp.pi/2)

q_23 = q_eje('z', Theta_3)

P_01p = Quaternion(0,0,0,l1+l2)

P_12 = Quaternion(0,0,0,d2)

P_23 = Quaternion(0,0,0,-l3)

T_23 = qtras_rot(q_23, Quaternion(0,0,0,0), P_23)

T_13 = qtras_rot(q_12, T_23, P_12)

T_1p3 = qtras_rot(q_1p1, T_13, Quaternion(0,0,0,0))

T_03 = qtras_rot(q_01p, T_1p3, P_01p).simplify()

qprint(T_03)

print('\n')

R_13 = q_12.mul(q_23)

R_1p3 = q_1p1.mul(R_13)

R_03 = (q_01p.mul(R_1p3)).simplify()

qprint(R_03)
