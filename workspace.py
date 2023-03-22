import sympy
import numpy
from cuaterniones import *
from Utilities import *
from Matrices import *
from sympy import pi
from sympy import Matrix
from sympy import Quaternion
from sympy import pprint
from sympy import cos
from sympy import sin

# SIMBOLICO -----------------------------------------#

nx, ny, nz = sp.symbols('nx ny nz')
ox, oy, oz = sp.symbols('ox oy oz')
ax, ay, az = sp.symbols('ax ay az')

p1x, p2x, p3x = sp.symbols('p1x p2x p3x')
p1y, p2y, p3y = sp.symbols('p1y p2y p3y')
p1z, p2z, p3z = sp.symbols('p1z p2z p3z')

noa = sp.Matrix([[nx, ox, ax],
                 [ny, oy, ay],
                 [nz, oz, az]])

l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
Theta , Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')
Gamma, Gamma_1 = sp.symbols('Gamma Gamma_1')
phi = sp.symbols('phi')
zeta = sp.symbols('zeta')
alpha = sp.symbols('alpha')
q0, q1, q2, q3 = sp.symbols('q0 q1 q2 q3')
a1, a2 = sp.symbols('a1 a2')
nx, ny, nz = sp.symbols('nx ny nz')
ox, oy, oz = sp.symbols('ox oy oz')
ax, ay, az= sp.symbols('ax ay az')

iden = sp.eye(3)
zero = [0,0,0]

q_identidad = Quaternion(1, 0, 0, 0)
#----------------------------------------------------#

