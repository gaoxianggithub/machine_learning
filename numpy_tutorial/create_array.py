import numpy as np

"""
Numpy也提供了很多方法去创建数组
"""
# 创建元素为0的2*2矩阵
a = np.zeros((2, 2))
print(a)
# 创建元素为1的1*2矩阵
b = np.ones((1, 2))
print(b)
# 创建元素为7的1*2矩阵
c = np.full((2, 2), 7)
print(c)
# 创建单位矩阵
d = np.eye(2)
print(d)
# 创建元素为随机数的1*2矩阵
e = np.random.random((2, 2))
print(e)
