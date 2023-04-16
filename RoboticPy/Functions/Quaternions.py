import sympy as sp
from sympy import Quaternion
from sympy import cos
from sympy import sin

def q_mul (cuaternions:list, post_or_pre : str) -> Quaternion | None:

    '''Multiplication of cuaternions coming from the list
    It is important to specify the order of multiplication:

    Post --> The multiplication goes from left to right.

    Pre --> The multiplication goes from right to left.
    '''

    if post_or_pre == 'pre':
        cuaternions.reverse()
        result = cuaternions[0]
        for cuaternion in cuaternions:
            if cuaternion == cuaternions[0]:
                continue
            else:
                result = result.mul(cuaternion)
        return result

    elif post_or_pre == 'post':
        result = cuaternions[0]
        for cuaternion in cuaternions:
            if cuaternion == cuaternions[0]:
                continue
            else:
                result = result.mul(cuaternion)
        return result

    else:
        print("Specify only 'post' or 'pre'.")

def q_rot (axis: str, angle) -> Quaternion | None:

    'Returns a basic rotation quaternion over X, Y or Z'

    axis = axis.lower()

    match axis:

      case 'x':
            return sp.Quaternion(sp.cos(angle/2),sp.sin(angle/2),0,0)
      case 'y':
            return sp.Quaternion(sp.cos(angle/2),0,sp.sin(angle/2),0)
      case 'z':
            return sp.Quaternion(sp.cos(angle/2),0,0,sp.sin(angle/2))
            
def q_T (axis: str, distance) -> Quaternion | None:

    'Returns a basic movement quaternion over X, Y or Z'

    axis = axis.lower()

    match axis:

      case 'x':
            return sp.Quaternion(0,distance,0,0)
      case 'y':
            return sp.Quaternion(0,0,distance,0)
      case 'z':
            return sp.Quaternion(0,0,0,distance)

def q_conj(cuaternion: Quaternion) -> Quaternion:

    'Returns the quaternion conjugate of the specified quaternion'

    return Quaternion(cuaternion.args[0], -cuaternion.args[1], -cuaternion.args[2], -cuaternion.args[3])

def q_print(cuaternion: Quaternion) -> None:

    'Prints on console the quaternion, with each element separated by commas. Useful for large quaternions'
    
    print('\n', cuaternion, '\n')
    
    for element in cuaternion.args:
        print(element)
        print('---------------------------')

def is_normalized(c: Quaternion) -> None:

    'Prints on console a warning that the specified quaternion is not normalized.'

    k = (sp.sqrt((c.a)**2 + (c.b)**2 + (c.c)**2 + (c.d)**2)).evalf(2)

    if k == 1:
        return None
    else:
        print('##########################################')
        print('The quaternion: ')
        print()
        print(c)
        print()
        print('is NOT normalized')
        print('##########################################')

def q_movil_T_R(cuaternion: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:

    '''Returns the result of the operation Movement(T) + Rotation refered to mobile axises.
    The result is the same to the operation Rotation + Movement(T) refered to fixed axises.

    Result_quaternion = Q · (0, v) · Q* + (0, P)

    Where:
     - Q is the rotation quaternion.
     - v is the vector refered to the mobile axises (u, v, w)
     - P is the position of the mobile axises refered to the fixed axises.
     - Q* is the conjugate of Q.
    '''

    is_normalized(cuaternion)
    multi = [cuaternion, v , q_conj(cuaternion)]

    return (q_mul(multi, 'post')).add(P)

def q_movil_R_T(cuaternion: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:

    '''Returns the result of the operation Rotation + Movement(T) refered to mobile axises:
    The result is the same to the operation Movement(T) + Movement refered to fixed axises.

    Result_vector = Q · (0, v + P) · Q* 
    
    Where:
     - Q is the rotation quaternion
     - v is the vector refered to the mobile axises (r, u, v)
     - P is the position of the mobile axises refered to the fixed axises.
     - Q* is the conjugate of Q.
    '''

    is_normalized(cuaternion)
    vector = Quaternion(0, v.b + P.b, v.c + P.c, v.d + P.d)

    multi = [cuaternion, vector ,q_conj(cuaternion)]

    return q_mul(multi, 'post')

def q_fijo_R_T(cuaternion: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:

    '''Returns the result of the operation Rotation + Movement(T) refered to fixed axises.
    The result is the same to the operation Movement(T) + Rotation refered to mobile axises.

    Result_quaternion = Q · (0, v) · Q* + (0, P)

    Where:
     - Q is the rotation quaternion.
     - v is the vector refered to the mobile axises (u, v, w)
     - P is the position of the mobile axises refered to the fixed axises.
     - Q* is the conjugate of Q.'''

    is_normalized(cuaternion)
    multi = [cuaternion, v , q_conj(cuaternion)]

    return (q_mul(multi, 'post')).add(P)

def q_fijo_T_R(cuaternion: Quaternion, v: Quaternion, P: Quaternion) -> Quaternion:

    '''Returns the result of the operation Movement(T) + Rotation refered to fixed axises:
    The result is the same to the operation Rotation + Movement(T) refered to mobile axises.

    Result_vector = Q · (0, v + P) · Q* 
    
    Where:
     - Q is the rotation quaternion
     - v is the vector refered to the mobile axises (r, u, v)
     - P is the position of the mobile axises refered to the fixed axises.
     - Q* is the conjugate of Q.
    '''

    is_normalized(cuaternion)
    vector = Quaternion(0, v.b + P.b, v.c + P.c, v.d + P.d)

    multi = [cuaternion, vector ,q_conj(cuaternion)]

    return q_mul(multi, 'post')

def q_norm (cuaternio: Quaternion, v: list) -> Quaternion:

    'Returns the normalized quaternion given a quaternion and the rotation axis.'

    k = sp.sqrt((v[0])**2 + (v[1])**2 + (v[2])**2)

    return Quaternion(cuaternio.a , cuaternio.b/k, cuaternio.c/k, cuaternio.d/k)

def q_sobre_eje(angle, v:list) -> Quaternion:

    'Returns the normalized rotation quaternion refered to a axis, given the angle of rotation.'
    
    cuaternion = Quaternion(cos(angle/2), v[0]*sin(angle/2), v[1]*sin(angle/2), v[2]*sin(angle/2))

    return q_norm(cuaternion, v)

