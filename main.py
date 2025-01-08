import sympy as sp
from sympy import pprint

from calc.kroneckerProduct import kroneckerProduct as kp
import constant as con
from eigen import eigen, print_eigen
from calc.matrix import matrix_intersection, dagger

x = con.pauli_X
z = con.pauli_Z
h = con.H
p = con.p
m = con.m
e = con.e
g = con.g
p = con.p
I = con.i
cnot = con.CNOT
z4 = con.z4
x4 = con.x4
z2 = con.z2
x2 = con.x2



if __name__ == '__main__':
    U = con.CNOT
    XI = kp(x,I)
    print_eigen(XI)
    pprint(U* sp.Matrix([[1], [0], [1], [0]]))
    pprint(U* sp.Matrix([[0], [1], [0], [1]]))
    print_eigen(x2)

