import sympy as sp
from sympy import pprint, Matrix

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

def eigen(matrix):
    if not isinstance(matrix,sp.Matrix):
        matrix = sp.Matrix(matrix)

    # 返回一个字典，键是特征值，值是特征值的代数重数
    eigenvals = matrix.eigenvals()
    # 返回一个列表，列表中的每个元素是一个三元组 (特征值, 重数, 特征向量)
    eigenvects = matrix.eigenvects()

    print("\n特征向量:")
    for eigenval, multiplicity, eigenvects in eigenvects:
        for eigenvect in eigenvects:
            print(f"特征值 {eigenval} 对应的特征向量: {eigenvect}")

    return eigenvals, eigenvects

    """
    计算两个包含 Matrix 对象的数组的交集。
    """
def matrix_intersection(arr1, arr2):
    intersection = []
    for mat1 in arr1:
        for mat2 in arr2:
            if mat1.equals(mat2):
                intersection.append(mat1)
                break  # 如果找到了相等的矩阵就跳出内循环，避免重复添加

    return intersection

if __name__ == '__main__':
    # 示例用法
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    matrix3 = Matrix([[1, 2], [3, 4]])
    matrix4 = Matrix([[9, 10], [11, 12]])

    arr1 = [matrix1, matrix2]
    arr2 = [matrix3, matrix4]

    result = matrix_intersection(arr1, arr2)
    print("交集结果:")
    for mat in result:
        print(mat)