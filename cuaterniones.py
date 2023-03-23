import sympy as sp
import numpy as np
from sympy import Quaternion
from sympy import pi
from sympy import cos
from sympy import sin

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

def q_rot (eje: str, angulo) -> Quaternion | None:
    'Devuelve un cuaternion básico de Rotación sobre X, Y o Z'

    eje = eje.lower()

    match eje:

      case 'x':
            return sp.Quaternion(sp.cos(angulo/2),sp.sin(angulo/2),0,0)
      case 'y':
            return sp.Quaternion(sp.cos(angulo/2),0,sp.sin(angulo/2),0)
      case 'z':
            return sp.Quaternion(sp.cos(angulo/2),0,0,sp.sin(angulo/2))
            
def q_T (eje: str, distancia) -> Quaternion | None:
    'Devuelve un cuaternion básico de Traslación sobre X, Y o Z'
    eje = eje.lower()

    match eje:

      case 'x':
            return sp.Quaternion(0,distancia,0,0)
      case 'y':
            return sp.Quaternion(0,0,distancia,0)
      case 'z':
            return sp.Quaternion(0,0,0,distancia)

def q_conj(cuaternion: Quaternion) -> Quaternion:
    'Devuelve el conjugado del cuaternio'

    return Quaternion(cuaternion.args[0], -cuaternion.args[1], -cuaternion.args[2], -cuaternion.args[3])

def q_print(cuaternion: Quaternion) -> None:
    'Printea el cuaternion y cada elemento separado por guiones'
    
    print('\n', cuaternion, '\n')
    
    for element in cuaternion.args:
        print(element)
        print('---------------------------')

def esta_normalizado(c: Quaternion) -> None:
    'Printea un aviso en caso de que el cuaternio no esté normalizado'
    k = (sp.sqrt((c.a)**2 + (c.b)**2 + (c.c)**2 + (c.d)**2)).evalf(2)

    if k == 1:
        return None
    else:
        print('##########################################')
        print('EL CUATERNIO: ')
        print()
        print(c)
        print()
        print('NO ESTA NORMALIZADO')
        print('##########################################')

def q_movil_T_R(cuaternio: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:
    '''Devuelve el vector resultado de la operación traslación + rotación respecto ejes móviles.
    Es igual que Rot. + Tras. respecto ejes fijos'''

    esta_normalizado(cuaternio)
    multi = [cuaternio, v , q_conj(cuaternio)]

    return (q_mul(multi, 'post')).add(P)

def q_movil_R_T(cuaternio: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:
    '''Devuevlve el vector resultado de la operación rotación + traslación respecto ejes móviles.
    Es igual que la operación Tras. + Ror. respecto a ejes fijos'''

    esta_normalizado(cuaternio)
    vector = Quaternion(0, v.b + P.b, v.c + P.c, v.d + P.d)

    multi = [cuaternio, vector ,q_conj(cuaternio)]

    return q_mul(multi, 'post')

def q_fijo_R_T(cuaternio: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:
    '''Devuelve el vector resultado de la operación rotación + traslación respecto ejes fijos.
    Es igual que Tras. + Rot. respecto ejes moviles'''

    esta_normalizado(cuaternio)
    multi = [cuaternio, v , q_conj(cuaternio)]

    return (q_mul(multi, 'post')).add(P)

def q_fijo_T_R(cuaternio: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:
    '''Devuevlve el vector resultado de la operación traslación + rotación respecto ejes fijos.
    Es igual que la operación Rot. + Tras. respecto a ejes moviles'''

    esta_normalizado(cuaternio)
    vector = Quaternion(0, v.b + P.b, v.c + P.c, v.d + P.d)

    multi = [cuaternio, vector ,q_conj(cuaternio)]

    return q_mul(multi, 'post')

def q_norm (cuaternio: Quaternion, v: list) -> Quaternion:
    'Devuelve el cuaternio normalizado dado el cuaternio y el vector sobre el que gira'
    k = sp.sqrt((v[0])**2 + (v[1])**2 + (v[2])**2)

    return Quaternion(cuaternio.a , cuaternio.b/k, cuaternio.c/k, cuaternio.d/k)

def q_sobre_eje(angle, v:list) -> Quaternion:
    'Devuelve cuaternion de giro alrededor de un eje un determinado ángulo. Se devuelve normalizado'
    
    cuaternio = Quaternion(cos(angle/2), v[0]*sin(angle/2), v[1]*sin(angle/2), v[2]*sin(angle/2))

    return q_norm(cuaternio, v)


# NOTAS IMPORTANTES LEER ----------------------------------------#

 ##################################################################
 #              RECUERDA NORMALIZAR CUATERNIOS                    #
 #################################################################

# Valores simbólicos--------------------------------------------#

#Cuaternio identidad = (1,0,0,0)

# l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
# Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
# d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')
# 
# Alpha = sp.symbols('Alpha')

#---------------------------------------------------------------#