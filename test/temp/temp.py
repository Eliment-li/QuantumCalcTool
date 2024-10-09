import sympy as sp
from sympy import pprint

import constant as con
from calc.kroneckerProduct import kroneckerProduct as kp

from eigen import eigen
x = con.pauli_X
z = con.pauli_Z
h = con.H
p = con.p
m = con.m
e = con.e
g = con.g
I = con.i
coeff = con.k
z4 = con.z4
x4 = con.x4
z2 = con.z2
x2 = con.x2


pprint(kp(x,I))
