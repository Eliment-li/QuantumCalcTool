import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
# 示例数据
people = ['Alice', 'Bob', 'Charlie']
# 每个人的时间段列表
time_slots = {
    'Alice': [(datetime(2024, 7, 13), datetime(2024, 7, 15))],
    'Bob': [(datetime(2024, 7, 14), datetime(2024, 7, 16))],
    'Charlie': [(datetime(2024, 7, 15), datetime(2024, 7, 17))]
}

# 创建图形和轴
fig, ax = plt.subplots(figsize=(10, 5))

# 绘制每个人的时间条
for i, person in enumerate(people):
    for j, (start_time, end_time) in enumerate(time_slots[person]):
        ax.plot([start_time, end_time], [i, i], marker='o', label=person if j == 0 else "")

# 设置 y 轴
ax.set_yticks(range(len(people)))
ax.set_yticklabels(people)

# 格式化 x 轴为日期格式
ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# 设置标签和标题
plt.xlabel('Date')
plt.ylabel('People')
plt.title('Schedules for Multiple People')

# 显示图例
plt.legend()

# 自动调整日期标签
fig.autofmt_xdate()

# 显示图形
plt.show()
