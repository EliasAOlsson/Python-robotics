import sympy as sp

from sympy import solve_poly_system
from sympy.abc import x, y
'''
solve_poly_system([x*y - 2*y, 2*y**2 - x**2], x, y)

sympy.solvers.solvers.nsolve -> Resolución métodos numéricos: 

    sp.nsolve(ecuaciones, (Theta, phi, alpha), (1,1,1), verify=False)

Consola: [(0, 0), (2, -sqrt(2)), (2, sqrt(2))] -> Vienen en el mismo orden que el 
orden que hemos dado de argumentos.
'''

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
#----------------------------------------------------#
'''for elemento in solucion:
    print(elemento)
    print('-------------------------------')'''

'''e1 = -1.87*ny + 3.22*oy +0.39*ay - 2
e2 = 0.92*ny + 3.35*oy + 0.73*ay - 2

e4 = -0.9*ny + 5.1*oy + 2.26*ay -2

e6 = -1.82*nz + 1.55*oz + 1.53*az -2.73
e7 = nx*ox + ny*oy + nz*oz
e8 = ax*ox + ay*oy + az*oz
e9 = ax*nx + ay*ny + az*nz

e10 = sp.sqrt(nx**2 + ny**2 + nz**2) - 1
e11 = sp.sqrt(ox**2 + oy**2 + oz**2) - 1'''

