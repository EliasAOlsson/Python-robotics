import sympy as sp
import math as mt
import numpy as np
from sympy import Quaternion

def quatmul (cuaterniones:list, post_or_pre : str) -> Quaternion | None:
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

def quat_eje (eje: str, angulo) -> Quaternion | None:
    'Devuelve un cuaternion básico de giro sobre X, Y o Z'

    eje = eje.lower()

    match eje:

      case 'x':
            return sp.Quaternion(sp.cos(angulo/2),sp.sin(angulo/2),0,0)
      case 'y':
            return sp.Quaternion(sp.cos(angulo/2),0,sp.sin(angulo/2),0)
      case 'z':
            return sp.Quaternion(sp.cos(angulo/2),0,0,sp.sin(angulo/2))
            
def conjugado(cuaternion: Quaternion) -> Quaternion:
    'Devuelve el conjugado del cuaternio'

    return Quaternion(cuaternion.args[0], -cuaternion.args[1], -cuaternion.args[2], -cuaternion.args[3])

def qprint(cuaternion: Quaternion) -> None:
    'Printea el cuaternion y cada elemento separado por guiones'
    
    print('\n', cuaternion, '\n')
    
    for element in cuaternion.args:
        print(element)
        print('---------------------------')

# NOTAS IMPORTANTES LEER ****
'''
 - Llamar a la función quat_eje con el ángulo SIN dividir entre 2

'''
#Cuaternio identidad = (1,0,0,0)

iden = Quaternion(1, 0, 0, 0)

#Valores simbólicos
l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')

Alpha = sp.symbols('Alpha')

#IMPORTANTE -> Recuerda el uso de .simplify()

Q_1 = quat_eje('z', Theta_1)
Q_2 = quat_eje('x', ((sp.pi/2)-(Alpha)))

print(Q_1)
print(Q_2)

print('\n')

qprint(quatmul([Q_1, Q_2], 'post'))


