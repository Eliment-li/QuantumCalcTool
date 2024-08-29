import sympy as sp
from sympy import pprint

'''
将两个矩阵的元素逐个相除得到一个新的矩阵
'''
def divide(A,B):
    # 检查两个矩阵的尺寸是否相同
    if A.shape != B.shape:
        raise ValueError("矩阵 A 和 B 必须具有相同的尺寸")

    # 元素逐个相除
    result = sp.Matrix([[
    1 if (A[i, j] == 0 and B[i, j] == 0)
    else (A[i, j] / B[i, j] if B[i, j] != 0
    else float('inf'))
    for j in range(A.cols)
] for i in range(A.rows)])

    return result

def dagger(M:sp.Matrix):
    M = M.conjugate() #共轭
    M = M.transpose() # 转置
    return M
'''
    求解向量 v 被向量组 vectors 线性表示的系数。

    参数:
    v (list or tuple): 目标向量
    vectors (list of lists or tuples): 向量组

    返回:
    dict: 系数的解
'''
def linear_combination_solver(v, vectors):
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

if __name__ == '__main__':
    M = sp.Matrix([
        [1+2j,3],
        [4,5]
    ],dtype=complex)
    pprint(dagger(M))
