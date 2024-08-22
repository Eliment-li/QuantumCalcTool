import sympy as sp
from calc.kroneckerProduct import kroneckerProduct as kp
from constant import Constant as con

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


def testsympy():
    # 定义符号变量 k
    k = sp.Symbol('k')
    # 定义表达式 k = sqrt(2)
    expr = sp.sqrt(2)

    k_expr = k + k
    print(k_expr)

if __name__ == '__main__':
    testsympy()