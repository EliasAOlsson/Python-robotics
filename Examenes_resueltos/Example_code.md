""" A1 = [[Theta_1, 475, 150, -pi/2],
               [Theta_2-pi/2, 0, 600, 0],
               [Theta_3-Theta_2, 0, 120, -pi/2],
               [Theta_4, 720, 0, -pi/2],
               [Theta_5, 0, 0, -pi/2],
               [Theta_6+pi, 85, 0 ,0]]
    
    result = Denavit(A1)
    rotacion, pos = extract_rot_vector(result)

    pprint(pos[2])
     """

_______________________________________________________________________________



 
    
    
    a = Matrix([0.4083, 0.8165, 0.4083])
    n = Matrix([0.8944, -0.4473, 0])
    o = a.cross(n)
    
    print(o)

    M_01 = m_T('y', 2) * m_Rot('z', Theta_1)
    M_12 = m_Rot('x', pi/2)* m_Rot('z', Theta_2)
    M_23 = m_T('x', -0.5)*m_Rot('z', Theta_3)
    M_34 = m_T('x', -0.5)*m_Rot('z', Theta_4)
    M_4n = m_T('x', -0.5)

    M_02 = M_01 * M_12

    M_03 = M_02 * M_23

    M_04 = M_03 * M_34

    M_0n = M_04 * M_4n

    pprint(sp.simplify(M_01))

    pprint(sp.simplify(M_02))

    pprint(sp.simplify(M_03))

    pprint(sp.simplify(M_04))

    pprint(sp.simplify(M_0n))
    