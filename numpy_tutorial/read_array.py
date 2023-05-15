import numpy as np

"""
Numpy是Python中科学计算的核心库。它提供了一个高性能的多维数组对象，以及用于
处理这些数组的工具。如果你已经熟悉MATLAB，你可能会发现本教程对开始使用Numpy
很有用。 numpy数组是一个由相同类型的值组成的网格，由非负整数元组索引。维数是
数组的秩；数组的形状是一个整数元组，给出了数组沿每个维度的大小。 我们可以从嵌
套的Python列表中初始化numpy数组，并使用方括号访问元素：
"""
a = np.array([1, 2, 3])  # Create a rank 1 array
print(a)
print(type(a))  # Prints "<class 'numpy.ndarray'>" ndarray 多维数组
print(a.shape)  # Prints "(3,)" 可以理解为几行几列 a只有一行，所以只有一个坐标
print(a[0], a[1], a[2])  # Prints "1 2 3"
a[0] = 5  # Change an element of the array
print(a)  # Prints "[5, 2, 3]"

b = np.array([[1, 2, 3], [4, 5, 6]])  # Create a rank 2 array
print(b.shape)  # Prints "(2, 3)"
print(b[0, 0], b[0, 1], b[1, 0])
