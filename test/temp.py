import sympy as sp

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
    symbols_demo()