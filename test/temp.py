import sympy as sp
from sympy import pprint

import constant as con
from calc.kroneckerProduct import kroneckerProduct as kp
def linear_combination_solver(v, vectors):
    """
    求解向量 v 被向量组 vectors 线性表示的系数。

    参数:
    v (list or tuple): 目标向量
    vectors (list of lists or tuples): 向量组

    返回:
    dict: 系数的解
    """
    # 将输入的向量转换为 sympy 矩阵
    v = sp.Matrix(v)
    U = sp.Matrix.hstack(*[sp.Matrix(vec) for vec in vectors])

    # 定义待求解的系数符号
    coeffs = sp.symbols(f'c1:{len(vectors) + 1}')
    c_matrix = sp.Matrix(coeffs)

    # 构造线性方程组
    equations = U * c_matrix - v

    # 求解线性方程组
    solution = sp.solve(equations, coeffs)

    return solution


h = con.H
g = con.g
e = con.e
p = con.p
m = con.m
gg = con.g2
ee = con.e2
sqrt_1_2 = con.sqrt_1_2

psy = sqrt_1_2*(kp(e,g)+kp(g,e))

result = linear_combination_solver(psy,[kp(p,p),kp(m,m)])

pprint(result)