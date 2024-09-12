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
coeff = con.k
z4 = con.z4
x4 = con.x4
z2 = con.z2
x2 = con.x2

a = sp.symbols('a')
b = sp.symbols('b')


fsi = a*kp(g,g,g)+ b * kp(e,e,e)

p0 = kp(g,g,g) * kp(g,g,g).transpose() + kp(e,e,e) * kp(e,e,e).transpose()
p1 = kp(e,g,g) * kp(e,g,g).transpose() + kp(g,e,e) * kp(g,e,e).transpose()

pprint(p1)

print(sp.latex(fsi * fsi.transpose()))

err_fsi = a*kp(e,g,g)+ b * kp(g,e,e)

measure_result = err_fsi.transpose() * p1 * err_fsi

pprint(measure_result)
pprint(p1 * fsi)

###333
