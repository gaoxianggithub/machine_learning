import numpy as np
import matplotlib.pyplot as plt

# # 计算正弦曲线上的点的x和y坐标
# x = np.arange(0, 3 * np.pi, 0.1)
# y = np.sin(x)
#
# # 使用matplotlib绘制点
# plt.plot(x, y)
# plt.show()  # 必须调用plt.show()才能显示图形。

x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()
