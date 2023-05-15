import numpy as np
from scipy.spatial.distance import pdist, squareform

# 创建以下数组，其中每行是2D空间中的一个点：
# [[0 1]
#  [1 0]
#  [2 0]]
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

# 计算x的所有行之间的欧几里得距离。
# d[i, j]是x[i, :]和x[j, :]之间的欧几里得距离，
# 并且d是以下数组：
# [[ 0.          1.41421356  2.23606798]
#  [ 1.41421356  0.          1.        ]
#  [ 2.23606798  1.          0.        ]]
d = squareform(pdist(x, 'euclidean'))
print(d)
