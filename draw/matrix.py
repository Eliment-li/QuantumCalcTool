import sympy as sp
import matplotlib.pyplot as plt
import matplotlib as mpl
from io import BytesIO
import base64


def matrix_to_image(matrix_data):
    try:
        # 设置全局字体大小
        mpl.rcParams.update({'font.size': 12})

        # 解析输入的矩阵数据
        matrix = sp.Matrix(matrix_data)
        rows, cols = matrix.shape

        # 计算合适的图形大小
        max_cell_width = max(len(str(matrix[i, j])) for i in range(rows) for j in range(cols))
        fig_width = max(cols * (max_cell_width * 0.15 + 0.5), 6)
        fig_height = max(rows * 0.6, 4)

        # 创建图形
        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        ax.axis('off')

        # 准备表格数据
        cell_text = [[str(matrix[i, j]) for j in range(cols)] for i in range(rows)]

        # 创建表格
        table = plt.table(
            cellText=cell_text,
            colLabels=[str(j) for j in range(cols)],  # 列标题
            rowLabels=[str(i) for i in range(rows)],  # 行标题
            loc='center',
            cellLoc='center',
            bbox=[0, 0, 1, 1]  # 表格占满整个图形
        )

        # 设置表格样式
        table.auto_set_font_size(False)
        table.set_fontsize(10)

        # 自动调整列宽
        for j in range(cols):
            max_len = max(len(str(matrix[i, j])) for i in range(rows))
            table.auto_set_column_width(j)

        # 设置行高
        for key, cell in table.get_celld().items():
            cell.set_height(0.3)

        # 设置隔行灰色背景
        for i in range(rows):
            for j in range(cols):
                if i % 2 == 0:  # 偶数行
                    table[(i + 1, j)].set_facecolor('#f8f8f8')

        # 设置标题样式
        for j in range(cols):
            table[(0, j)].set_facecolor('#e8e8e8')
            table[(0, j)].set_text_props(weight='bold', fontsize=11)

        for i in range(rows):
            table[(i + 1, -1)].set_facecolor('#e8e8e8')
            table[(i + 1, -1)].set_text_props(weight='bold', fontsize=11)

        # 设置单元格边框
        for key, cell in table.get_celld().items():
            cell.set_edgecolor('#cccccc')
            cell.set_linewidth(0.5)

        # 调整布局

        # 转换为 base64 编码的图像
        buf = BytesIO()
        plt.show()

        return base64.b64encode(buf.getvalue()).decode('utf-8')
    except Exception as e:
        return {"error": str(e)}
