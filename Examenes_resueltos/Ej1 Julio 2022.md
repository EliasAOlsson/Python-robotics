T_13 = Matrix([[0,1,0,1],
               [-1,0,0,1],
               [0,0,1,1],
               [0,0,0,1]])

R_13, P_13 = extrae_Rot_Vector(T_13)

R_12 = Matrix([[1,0,0],
               [0,0,-1],
               [0,-1,0]])

R_23 = ((R_12)**(-1)) @ (R_13)
P_23 = [3,2,1]

T_23 = m_homogenea(R_23, P_23)

#--------------------------

T_12 = T_13 @ (T_23 **(-1))

#-------------------------

R_02 = sp.Matrix([[0, 0, 1],
                 [1, 0, 0],
                 [0, 1, 0]])

R_20 = R_02.T

T_02 =m_homogenea(R_02, [1,3,-2])

T_20 = T_02 ** (-1)

# -------------------

T_03 = T_02 @ T_23

pprint(T_03)