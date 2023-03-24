## En matrices: 

A = sp.Matrix([[-0.9932, 0.0673, 0.093],
               [ny, 0.7472, ay],
               [nz, 0.6612, az]])


a = sp.Matrix([0.093, ay, az])

n = sp.Matrix([-0.9932, ny, nz])

o = a.cross(n)

print(o)

A_Final = sp.Matrix([[-0.9932, 0.0673, 0.093],
               [0.112111281818586, 0.7472, 0.655229209414893],
               [-0.0313218851443124, 0.6612, -0.749382868185239]])

Matrizfinal = sp.Matrix([[0, -(sp.sqrt(2)/2), (sp.sqrt(2)/2)],
                         [1, 0, 0],
                         [0, (sp.sqrt(2)/2), (sp.sqrt(2)/2)]])

solucion = multiplicador(3, 'post', [A_Final.T, Matrizfinal]).evalf(3)

sp.pprint(solucion)

## En Sistema de ecuaciones

e1 = ny**2 + nz**2 - 0.01355 #-1 +(0.9932)**2

e2 = ay**2 + az**2 - 0.9909 #-1 +0.095**2

e3 = -0.9932*az - 0.093*nz - 0.7472

e4 = 0.9932*ay + 0.093*ny - 0.6612

ecuaciones = [e1,e2, e3, e4]

solucion = sp.solve(ecuaciones, ny, nz, ay, az)



print(solucion)
