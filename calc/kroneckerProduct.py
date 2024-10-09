import numpy as np
from pprint import pprint
import sympy as sp
e = sp.Matrix([0, 1], dtype=int)
g = sp.Matrix([1, 0], dtype=int)

i = sp.Matrix([
    [1, 0],
    [0, 1]
])

# define sqrt (1/2)
k = sp.Symbol('1/2')
sqrt_1_2 = sp.sqrt(k)

e = sp.Matrix([0, 1], dtype=int)
g = sp.Matrix([1, 0], dtype=int)

p = (sqrt_1_2 * g) + (sqrt_1_2 * e)
m = (sqrt_1_2 * g) - (sqrt_1_2 * e)

pauli_X = sp.Matrix([
    [0, 1],
    [1, 0]
])

pauli_Y = sp.Matrix([
    [0, -1j],
    [1j, 0]
])

pauli_Z = sp.Matrix([
    [1, 0],
    [0, -1]
])

S = sp.Matrix([
    [1, 0],
    [0, 1j]
])

T = sp.Matrix([
    [1, 0],
    [0, np.exp(1j * np.pi / 4)]
])

H = sqrt_1_2 * sp.Matrix([
    [1, 1],
    [1, -1]
])

CNOT = sp.Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0]
])


#test
#np.kron(g, e)
'''
本函数计算张量积，又叫直积或 Tensor Product, Kronecker Product,
可以用 0 代表 g, 1 代表 e
多个对象可放在一个数组里， 例如 items = [g, g, g, g], 则计算 |gggg>
'''
def kroneckerProduct(*args):
    #接收字符串形式的输入 例如 00000
    if len(args) == 1 and isinstance(args[0], str):
        items = string2kroneckerProduct(args[0])
    else:
        items = list(args)
    #获取第一个项
    result = items[0]
    if result == 0:
        result = g
    if result == 1:
        result = e
    #和后面的项依次做张量运算
    for i in range(1, len(items)):
        if items[i] == 0:
            items[i] = g
        if items[i] == 1:
            items[i] = e
        result = sp.kronecker_product(result, items[i])
    return result

map = {
    '0':g,
    '1':e,
    'x':pauli_X,
    'y':pauli_Y,
    'z':pauli_Z,
}

def string2kroneckerProduct(str):
    items =[]
    for char in str:
        items.append(map[char])
    return items

z4 = kroneckerProduct(pauli_Z, pauli_Z, pauli_Z, pauli_Z)
x4 = kroneckerProduct(pauli_X, pauli_X, pauli_X, pauli_X)
z2 = kroneckerProduct(pauli_Z, pauli_Z)
x2 = kroneckerProduct(pauli_X, pauli_X)

if __name__ == '__main__':
    pass