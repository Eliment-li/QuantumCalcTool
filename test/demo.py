import  numpy as np
import sympy as sp
from sympy import pprint

from calc import matrix
import constant as con
from calc.kroneckerProduct import kroneckerProduct as kp
from calc.matrix import dagger
from eigen import eigen
x = con.pauli_X
z = con.pauli_Z
h = con.H
p = con.p
m = con.m
e = con.e
g = con.g
coeff = con.k
z4 = con.z4
x4 = con.x4
z2 = con.z2
x2 = con.x2

#验证 pauli x y z 的 乘以自身的共轭转置都等于i ，例如 X@X_dagger = I

'''
h 门 可以将 |+> 转为 |0> 
因此，执行pauli_X 可以先执行 H 再 执行 z 来实现

coeff = np.sqrt(1 / 2)
p = (coeff * g) + (coeff * e)
'''
def p_to_0():
    x = con.pauli_X
    h = con.H
    p = con.p
    print(p)
    print(p @ h )
    print(p @ h @ h)


'''
验证 4 比特 stabilizer 的 测量结果
'''
def test_stabilizer():

    x_stabilizer = kp(x,x,x,x)
    z_stabilizer = kp(z,z,z,z)

    state = kp(m,m,p,m)
    print(state)
    # sp.pretty_print(x_stabilizer)
    result =  x_stabilizer * state
    print(result)
    print(matrix.divide(result, state))

'''
验证 2 比特 stabilizer 共用本征态
Table 2
'''
def test_2qubits_stabilizer():

     #|ge> + |eg>
    state = sp.Matrix(kp(g,e)) + sp.Matrix(kp(e,g))

    zz = kp(z,z)
    xx = kp(x,x)
    gg = kp(g,g)

    print(f'|ge> + |eg> = {sp.pretty(state.T)}')
    print(f' zz * state = { zz * state}')
    print(f' xx * state  = {xx  * state}')

    print(f'gg  =\n{sp.pretty(gg.T)  }')
    print(f' xx * gg   = { xx* gg}')

    print(kp(g,g))
    print(kp(e,e))
    print(kp(g, e))
    print(kp(e,g))
    print(kp(z,z))
    eigen(kp(z,z))

'''
验证 x2 z2 , x4 z4 的可交换性
'''
def swappable_matrix():
    print(np.array_equal(z4 @ x4, x4 @ z4))
    print(np.array_equal(z2 @ x2, x2 @ z2))


def test_anti_commute():
    PI = sp.pi
    i = sp.I

    rx = sp.Matrix(
        [
            [sp.cos(PI/4), -i*sp.sin(PI/4)],
            [-i*sp.sin(PI/4), sp.cos(PI/4)]
        ]
    )

    rz = sp.Matrix(
        [
            [con.sqrt_1_2*(1-i),0],
            [0,con.sqrt_1_2*(1+i)]
        ]
    )

    rx = sp.Matrix([
        [1,-i],
        [-i,1]
    ])
    rz = sp.Matrix([
        [1-i,0],
        [0,1+i]
    ])
    XZ = rx*rz
    ZX = rz*rx

    pprint(con.pauli_X*con.pauli_Z)
    pprint(con.pauli_Z*con.pauli_X)
    # pprint(XZ)
    # pprint("========")
    # pprint(ZX)
    # pprint(XZ == -ZX)


if __name__ == '__main__':
    pass