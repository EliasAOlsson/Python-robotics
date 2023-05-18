    Q = sp.Quaternion(0.225, -0.2812, -0.9289, -0.086)

    R_06 = Cuat_a_mat(Q)
    
    M_06_numerica = Matrix([[-0.7405, 0.5611, -0.3696, 1062.88],
                   [0.4837, 0.8271, 0.2863, 656.154],
                   [0.4664, 0.03323, -0.8839, 275.605],
                   [0, 0, 0, 1]])
    
    Extremo_muneca = Matrix([0,0,-85,1])

    P_0muneca = M_06_numerica * Extremo_muneca

    Theta_1 = 30*pi/180
    Theta_2 = 60*pi/180
    Theta_3 = 45*pi/180

    
    denavit_03 = [[Theta_1, 475, 150, -pi/2],
                  [Theta_2-pi/2, 0, 600, 0],
                  [Theta_3-Theta_2, 0, 120, -pi/2]]
    
    denavit_36 = [[Theta_4, 720, 0, pi/2],
                  [Theta_5, 0, 0, -pi/2],
                  [Theta_6+pi, 85, 0, 0]]

    M_03 = Denavit(denavit_03)

    M_36 = Denavit(denavit_36)

    sp.simplify(M_03)
    
    R_03, P_03 = extract_rot_vector(M_03)

    R_30 = R_03.T

    R_36 = R_30 * R_06

    pprint(R_36.evalf(4))

    '''
    R_03 = Matrix([[0,0,1],
                   [0,-1,0],
                   [1,0,0]])
    
    R_30 = R_03.T

    R_36 = R_30 * R_06

    pprint(R_36.evalf(4))'''