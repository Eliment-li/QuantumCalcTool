import numpy as np
from calc.kroneckerProduct import kroneckerProduct as kp
import sympy as sp
from sympy import sqrt, pprint

i = sp.Matrix([
    [1, 0],
    [0, 1]
])

# define sqrt (1/2)
k = sp.Symbol('1/2')
sqrt_1_2 = sp.sqrt(k)

e = sp.Matrix([0, 1], dtype=int)
g = sp.Matrix([1, 0], dtype=int)

e2 = kp(e, e)
g2 = kp(g, g)

p = (sqrt_1_2 * g) + (sqrt_1_2 * e)
m = (sqrt_1_2 * g) - (sqrt_1_2 * e)

p2 = kp(p, p)
m2 = kp(m, m)

pauli_X = sp.Matrix([
    [0, 1],
    [1, 0]
])

pauli_Y = sp.Matrix([
    [0, -1j],
    [1j, 0]
])

pauli_Z = sp.Matrix([
    [1, 0],
    [0, -1]
])

S = sp.Matrix([
    [1, 0],
    [0, 1j]
])

T = sp.Matrix([
    [1, 0],
    [0, np.exp(1j * np.pi / 4)]
])

H = sqrt_1_2 * sp.Matrix([
    [1, 1],
    [1, -1]
])

CNOT = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])

z4 = kp(pauli_Z, pauli_Z, pauli_Z, pauli_Z)
x4 = kp(pauli_X, pauli_X, pauli_X, pauli_X)
z2 = kp(pauli_Z, pauli_Z)
x2 = kp(pauli_X, pauli_X)

# rz = sp.Matrix([
    #
    #     [1-I,0],[0,1+I]
    # ])
    #
    # rx = sp.Matrix([
    #     [1,-I],[-I,1]
    # ])
    #
    # print(simplify(rz*rx*rz))
    #
    # print(I*I)
if __name__ == '__main__':
    pprint(sqrt_1_2)