from sympy.printing import pprint
from constant import Constant as con
from calc.kroneckerProduct import kroneckerProduct as kp
x = con.pauli_X
z = con.pauli_Z
h = con.H
p = con.p
m = con.m
e = con.e
g = con.g
e2 = con.e2
g2 = con.g2
p = con.p
i = con.i

cnot = con.CNOT
z4 = con.z4
x4 = con.x4
z2 = con.z2
x2 = con.x2

if __name__ == '__main__':
    s = (e2+g2) * con.k

    pprint(z2 @ s)


