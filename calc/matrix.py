import sympy as sp

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