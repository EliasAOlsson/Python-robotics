# Useful sympy commands

``` python

print(matriz_i[-2][0]) # -> Access operator to N-dimensional arrays

print(Multi[-2,3]) # -> Access operator to matrices

pprint(*matrix*) # -> Sympy function that allows "prety" printintg. Specially useful for printing matrices.

matrix_a.dot(matrix_b) # -> "dot" product of matrices

matrix_a.cross(matrix_b) # -> "Cross" product of matrices

```

## __Usage of main__

All the code you want to implement should be indented into the 'if __name_ _' function. Make sure you make a correct use of the functions for your problem.

## __Denavit__

Example code: 

````python

Data = [[pi/2+pi, l1, -l2, -pi/2],
        [0, 0, -l3, pi],
        [0, 0, l4, 0],
        [pi/2, 0, 0, -pi/2], 
        [pi/2, l5, 0, 0]]
        
Complete_print(Data)

````

## __Matrices__

Basic matrix rotation
```` 
   u      v      w
| n_x    o_x    a_x| x
| n_y    o_y    a_y| y
| n_z    o_z    a_z| z
````
Source = https://en.wikipedia.org/wiki/Rotation_matrix

Every component represents the cosine of the angle between the fixed axis (our reference [x, y, z]) and the axis of our rotating coordinate system [u, v, z].

n_x = cos(alpha)

Being alpha the angle between U and X

### __Properties__

The "dot" product of every file in the matrix should NOT be superior to 1.
This means that:

[ 0 0 0 ] -> Is NOT possible

[ 0 1 0 ] -> IS possible

[ 0 2 0 ] -> Is NOT possible

M ^-1 = M ^T

The rotation matrix of u,v,w with x,y,z as reference is the inverted matrix of x,y,z with u,v,z as reference.

## __Quaternions__

For more information about quaternions: https://en.wikipedia.org/wiki/Quaternion.

## __Sistema_ecuaciones__

A basic implementation of a linear equation solver (It's from sympy)

## __Utils__

This includes some useful functions that are used across the rest of the scripts.
