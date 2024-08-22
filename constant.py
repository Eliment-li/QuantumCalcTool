import numpy as np
from kroneckerProduct import kroneckerProduct as kp
import sympy as sp
from sympy import I, simplify, symbols
from sympy import sqrt
class Constant:
    i = sp.Matrix([
        [1,0],
        [0,1]
    ])


    #k = np.sqrt(1 / 2)
    k = sqrt(1/2)
    e = sp.Matrix([0,1],dtype=int)
    g = sp.Matrix([1,0],dtype=int)

    p = (k * g) + (k * e)
    m = (k * g) - (k * e)

    pauli_X = sp.Matrix([
        [0,1],
        [1,0]
    ])


    pauli_Y = sp.Matrix([
        [0,-1j],
        [1j,0]
    ])

    pauli_Z = sp.Matrix([
        [1,0],
        [0,-1]
    ])

    S = sp.Matrix([
        [1,0],
        [0,1j]
    ])

    T = sp.Matrix([
        [1, 0],
        [0, np.exp(1j * np.pi / 4)]
    ])


    H = k * sp.Matrix([
        [1,1],
        [1,-1]
    ])

    CNOT = sp.Matrix([
        [1,0,0,0],
        [0,1,0,0],
        [0,0,0,1],
        [0,0,1,0]
    ])


    z4 = kp(pauli_Z,pauli_Z,pauli_Z,pauli_Z)
    x4 = kp(pauli_X,pauli_X,pauli_X,pauli_X)
    z2 = kp(pauli_Z,pauli_Z)
    x2 = kp(pauli_X,pauli_X)



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
    sqrt2 = sqrt(2)
    print(sqrt2*sqrt2)
