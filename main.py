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
    simulator = AerSimulator()
    #create a quantum circuit
    qc = qiskit.QuantumCircuit(5,1)

    '''
    只有 X 门(bit-flip error) 会影响测量结果 Z 门不会
    '''
    #qc.x(1)
    qc.cx(1,0)
    qc.cx(2,0)
    qc.cx(3,0)
    qc.cx(4,0)

    # Measure only qubit 0 and store the result in classical bit 0
    qc.measure(0, 0)

    #qc = transpile(qc, simulator)
    result = simulator.run(qc).result()
    counts = result.get_counts(qc)
    print(counts)
    #print(qc.draw())
    #plot_histogram(counts).show()


