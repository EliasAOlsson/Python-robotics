import sympy as sp
from Functions.Quaternions import *
from Functions.Utils import *
from Functions.Matrices import *
from Functions.Denavit import *

if __name__ == '__main__':
    
    # SIMBOLIC (IGNORE) -----------------------------------------#

    'You can use any of the keywords specified below as simbolic values. You can add more following the same structure.'

    """ nx, ny, nz = sp.symbols('nx ny nz')
    ox, oy, oz = sp.symbols('ox oy oz')
    ax, ay, az = sp.symbols('ax ay az')
    p1x, p2x, p3x = sp.symbols('p1x p2x p3x')
    p1y, p2y, p3y = sp.symbols('p1y p2y p3y')
    p1z, p2z, p3z = sp.symbols('p1z p2z p3z') 
    noa = sp.Matrix([[nx, ox, ax],
                     [ny, oy, ay],
                     [nz, oz, az]])"""
    l1 , l2, l3, l4, l5, l6, l7 = sp.symbols('l1 l2 l3 l4 l5 l6 l7')
    Theta , Theta_1, Theta_2, Theta_3, Theta_4, Theta_5, Theta_6, Theta_7 = sp.symbols('Theta Theta_1 Theta_2 Theta_3 Theta_4 Theta_5 Theta_6 Theta_7')
    d1 , d2, d3, d4, d5, d6, d7 = sp.symbols('d1 d2 d3 d4 d5 d6 d7')
    """Gamma, Gamma_1, phi, zeta, alpha, q0, q1, q2, q3, a1, a2= sp.symbols('Gamma Gamma_1 phi zeta alpha q0 q1 q2 q3 a1 a2')
     nx, ny, nz = sp.symbols('nx ny nz')
    ox, oy, oz = sp.symbols('ox oy oz')
    ax, ay, az= sp.symbols('ax ay az') """
    iden = sp.eye(3)
    zero = [0,0,0]
    q_identidad = Quaternion(1, 0, 0, 0)
    q_zero = Quaternion(0,0,0,0)
    #-------------------------------------------------
    
    'Write here your code'

    