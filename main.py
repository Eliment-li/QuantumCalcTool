import sympy as sp
from sympy import pprint

from calc.kroneckerProduct import kroneckerProduct as kp
import constant as con
from eigen import eigen, print_eigen
from calc.matrix import matrix_intersection, dagger
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

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

import  qiskit

if __name__ == '__main__':
  xaxb = kp(x, x)
  psi = kp(g, g)+kp(e,e)

  print(psi == xaxb*psi)


