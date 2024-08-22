import numpy as np
from pprint import pprint
import sympy as sp


#test
#np.kron(g, e)
'''
计算张量积，又叫直积或 Tensor Product, Kronecker Product,
多个对象可放在一个数组里， 例如 items = [g, g, g, g]
'''
def kroneckerProduct(*args):
    items = list(args)
    result = items[0]
    for i in range(1, len(items)):
        result = sp.kronecker_product(result, items[i])
    return result


if __name__ == '__main__':
    pass