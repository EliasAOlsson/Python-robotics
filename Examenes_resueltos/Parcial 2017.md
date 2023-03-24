
# Parcial 2017

Ecuaciones= [m_T('y', 1),
             m_T('z', 1),
             m_Rot('z', -sp.pi/4),
             m_T('z', sp.sqrt(2)/2),
             m_Rot('x', -0.4636),
             m_T('y', 1)]

sp.pprint(multiplicador(4, 'post', Ecuaciones).evalf(3))'''


'''M = sp.Matrix([[0.290255180000000, -0.231013200000000, 0.928546320000000],
               [-0.417586000000000, 0.348728000000000, 0.357403200000000],
               [-0.406306320000000, -0.908212800000000, -0.0988728200000000]])

sp.pprint(multiplicador(3, 'post', [M, m_basica('x', -sp.pi/2)]))'''

