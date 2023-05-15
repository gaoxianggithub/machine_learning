import numpy as np
from PIL import Image

image_file = r'cat.png'
height = 300
img = Image.open(image_file)
img_width, img_height = img.size
width = int(1.8*height*img_width//img_height)
img = img.resize((width, height), Image.ANTIALIAS)
pixels = np.array(img.convert('L'))
print(pixels.shape)
print(pixels)
print('type(pixels):', type(pixels))
chars = "BEFA$OC?7>!:-;. "
N = len(chars)
step = 256//N
print(N)
result = ''
for i in range(height):
    for j in range(width):
        result += chars[pixels[i, j]//step]
    result += '\n'
with open('output.txt', 'w') as f:
    f.write(result)