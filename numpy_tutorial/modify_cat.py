from PIL import Image
import numpy as np
# 将JPEG图像读入numpy数组
with Image.open('../assets/cat.png') as im:
    im_resized = im.resize((300, 300))
    img_tinted = np.array(im) * np.array([1, 0.95, 0.9])
    im_resized.save('../assets/cat1.png')

# 我们可以通过将每个颜色通道乘以不同的标量常数来着色图像。图像的形状为（400, 248, 3）;
# 我们将其乘以形状为（3，）的数组[1，0.95，0.9]；
# numpy广播意味着这会使红色通道保持不变，
# 并将绿色和蓝色通道分别乘以0.95和0.9

# 将着色的图像调整为300 x 300像素。

# 将着色的图像写回磁盘