import numpy as np
import sympy as sp
'''
first_eigenvector = eigenvectors[:, 0]
'''

def eigen(matrix):
    if not isinstance(matrix,sp.Matrix):
        matrix = sp.Matrix(matrix)

    # 返回一个字典，键是特征值，值是特征值的代数重数
    eigenvals = matrix.eigenvals()
    # 返回一个列表，列表中的每个元素是一个三元组 (特征值, 重数, 特征向量)
    eigenvects = matrix.eigenvects()
    return eigenvals, eigenvects


if __name__ == '__main__':
    zz = [[ 1,  0,  0,  0],
 [ 0, -1,  0,  0],
 [ 0,  0, -1,  0],
 [ 0,  0,  0,  1]]
    eigenvals, eigenvects = eigen(zz)
    print("\n特征向量:")
    for eigenval, multiplicity, eigenvects in eigenvects:
        for eigenvect in eigenvects:
            print(f"特征值 {eigenval} 对应的特征向量: {eigenvect}")


