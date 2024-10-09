import sympy as sp
from sympy import pprint

from calc.kroneckerProduct import kroneckerProduct as kp
import constant as con
from eigen import eigen
from calc.matrix import matrix_intersection

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

    g1 = kp(I,I,I,x,x,x,x)
    g2 = kp(I,x,x,I,I,x,x)
    g3 = kp(x,I,x,I,x,I,x)

    z1z2 = kp(z,z,I)
    z2z3  = kp(I,z,z)

    L0 = kp('0000000')+kp('1010101')+kp('0110011')+kp('1100110')+kp('0001111')+kp('1011010')+kp('0111100')+kp('1101001')
    #pprint(L0)
    print(g1 * L0 == L0)
    arr1 = []
    arr2 = []

    eigenvals, eigenvects = eigen(g1)
    for eigenval, multiplicity, eigenvects in eigenvects:
        if eigenval == 1:
            arr1 = eigenvects


    eigenvals2, eigenvects2 = eigen(g3)
    for eigenval2, multiplicity2, eigenvects2 in eigenvects2:
        if eigenval2 == 1:
            arr2 = eigenvects2

    for v in arr1:
        if L0.equals(v):
            print(v)
