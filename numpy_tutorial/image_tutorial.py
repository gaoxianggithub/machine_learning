import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

with Image.open('../assets/cat.png') as im:
    img_tinted = np.array(im) * np.array([1, 0.95, 0.9])
    plt.subplot(1, 2, 1)
    plt.imshow(im)
    plt.subplot(1, 2, 2)
    plt.imshow(np.uint8(img_tinted))
    plt.show()
