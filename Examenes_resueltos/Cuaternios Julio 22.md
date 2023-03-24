# OJO! Aquí las funciones eran TODAS ""respecto a ejes móviles"

Los movimientos entre los ejes 0-1 y 1-2 eran respecto a
ejes fijos, pero a la hora de hacer los scripts SOLO se tenían los referentes a ejes móviles (Al final las formulas TR moviles = RT fijos e igual con RT movil = TR Fijo, por lo que da igual pero es importante denotarlo)


Q_01 = q_rot('z', pi/2)
P_01 = Quaternion(0,1,1,1)

M_01 = qrot_tras(Q_01, q_zero, P_01)


#-----------------------

Q_12 = q_rot('x', pi/3)
P_12 = Quaternion(0,1,2,3)
M_12 = qtras_rot(Q_12, q_zero, P_12)

M_02 = qrot_tras(Q_01, M_12, P_01)


#---------------------------

Q_23 = q_rot('z', (2/3)*pi)
P_23 = Quaternion(0,2,2,2)

M_23 = qrot_tras(Q_23, q_zero, P_23)

M_13 = qtras_rot(Q_12, M_23, P_12)

M_03 = M_02 = qrot_tras(Q_01, M_13, P_01)

#---------------------
Q_34 = q_rot('y', pi/2)

P_34 = Quaternion(0,1,1,1)

M_34 = qtras_rot(Q_34, q_zero, P_34)

M_24 = qrot_tras(Q_23, M_34, P_23)

M_14 = qtras_rot(Q_12, M_24, P_12)

M_04 = M_02 = qrot_tras(Q_01, M_14, P_01)

print(M_04.evalf(3))