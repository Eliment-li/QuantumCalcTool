import sympy as sp
from sympy import pprint

import constant as con
from calc.kroneckerProduct import kroneckerProduct as kp

from eigen import eigen
x = con.pauli_X
x2 = con.x2
x4 = kp(x,x,x,x)

import tensorly as tl
import numpy as np
from tensorly.decomposition import parafac

# 目标向量
target_vector = np.array([0, -1, 1, 0])

# 将目标向量转换为张量
target_tensor = tl.tensor(target_vector.reshape(2, 2))  # 将其视为 2x2 张量

# 使用 CP 分解
factors = parafac(target_tensor, rank=2)

# 输出分解的因子
print("分解得到的因子:")
for i, factor in enumerate(factors):
    print(f"因子 {i + 1}:\n{factor}")

# 提取向量 a 和 b
a = factors[1][0]  # 第一个因子
b = factors[1][1]  # 第二个因子

# 计算张量积
tensor_product = tl.kron(a, b)

# 输出结果
print("找到的向量 a:", a)
print("找到的向量 b:", b)
print("张量积:", tensor_product)

# 检查是否等于目标向量
if np.array_equal(tensor_product, target_vector):
    print("找到的张量积等于目标向量。")
else:
    print("没有找到满足条件的张量积。")
