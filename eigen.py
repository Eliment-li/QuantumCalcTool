import numpy as np

'''
first_eigenvector = eigenvectors[:, 0]
'''
# def eigen(matrix):
#     eigenvalues, eigenvectors = np.linalg.eig(matrix)
#     for i in range(len(eigenvalues)):
#         eigenvector = eigenvectors[:, i]
#         result = f"特征值 {eigenvalues[i]} : {np.round(eigenvector,1)}"
#         print(result)
#     print(np.round(eigenvectors, 1))
#     return eigenvalues, eigenvectors

def eigen(matrix):
    # eigenvalues, eigenvectors = np.linalg.eig(matrix)

    # 计算特征值和特征向量
    eigenvals = matrix.eigenvals()  # 返回一个字典，键是特征值，值是特征值的代数重数
    eigenvects = matrix.eigenvects()  # 返回一个列表，列表中的每个元素是一个三元组 (特征值, 重数, 特征向量)

    print("\n特征向量:")
    for eigenval, multiplicity, eigenvects in eigenvects:
        for eigenvect in eigenvects:
            print(f"特征值 {eigenval} 对应的特征向量: {eigenvect}")

    return eigenvals, eigenvects


if __name__ == '__main__':
    zz = [[ 1,  0,  0,  0],
 [ 0, -1,  0,  0],
 [ 0,  0, -1,  0],
 [ 0,  0,  0,  1]]


