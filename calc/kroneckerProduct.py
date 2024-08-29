import numpy as np
from pprint import pprint
import sympy as sp
e = sp.Matrix([0, 1], dtype=int)
g = sp.Matrix([1, 0], dtype=int)

#test
#np.kron(g, e)
'''
本函数计算张量积，又叫直积或 Tensor Product, Kronecker Product,
可以用 0 代表 g, 1 代表 e
多个对象可放在一个数组里， 例如 items = [g, g, g, g], 则计算 |gggg>
'''
def kroneckerProduct(*args):
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


if __name__ == '__main__':
    pass