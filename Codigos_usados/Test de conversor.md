v1 = sp.Matrix([[0.6427, 0.616, 0.4562]])
v2 = sp.Matrix([[0.4275, -0.7815, 0.4544]])

v3 = v2.cross(v1)

sp.pprint(v3)