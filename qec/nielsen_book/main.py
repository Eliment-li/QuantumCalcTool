import math

import sympy as sp
from sympy import pprint

from calc.kroneckerProduct import kroneckerProduct as kp
import constant as con
x = con.pauli_X
z = con.pauli_Z
h = con.H
p = con.p
m = con.m
e = con.e
g = con.g
p = con.p
i = con.i
cnot = con.CNOT
z4 = con.z4
x4 = con.x4
z2 = con.z2
x2 = con.x2

def T(v):
    return v.transpose()
#outer_product
def op(v):
    return v * v.T


# 验证 nielsen P374 编码
def P374():
    p0 = op(kp(g,g,g)) + op(kp(e,e,e))
    p1 = op(kp(e,g,g)) + op(kp(g,e,e))
    p2 = op(kp(g,e,g)) + op(kp(e,g,e))
    p3 = op(kp(g,g,e)) + op(kp(e,e,g))

    psi = (kp(g,g,g) + kp(e,e,e)) * math.sqrt(1/2)

    pprint(psi.T * p0 * psi)
    pprint(psi.T * p1 * psi)
    pprint(psi.T * p2 * psi)
    pprint(psi.T * p3 * psi)

if __name__ == '__main__':
    print()

