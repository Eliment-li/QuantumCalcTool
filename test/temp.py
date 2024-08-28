import sympy as sp
from sympy import pprint
import  constant as con
from calc.kroneckerProduct import kroneckerProduct as kp
p = con.p
m = con.m

e = con.e
g = con.g
#展示 sympy 的根号用法
def symbols_demo():
    # 定义符号变量
    x = sp.symbols('2')

    # 定义根号表达式
    expr = sp.sqrt(x)

    # 打印表达式
    print("根号表达式:")
    sp.pprint(expr)

if __name__ == '__main__':
    pprint(kp(g,g))
    pprint(kp(g,e))
    pprint(kp(e,g))
    pprint(kp(e,e))