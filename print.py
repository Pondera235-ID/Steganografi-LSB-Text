from PIL import Image
import numpy as np

gambar = "alpro.bmp"
image = Image.open(gambar, 'r')
rgb_image = image.convert('RGB')
list1 = list(rgb_image.getdata())
list = np.array(rgb_image.getdata())
weight,height = rgb_image.size
#lists = list.reshape(5,5)
#print(list,list1)

print(list1[0:3])
print(list1[4:7])
print(list1[7:10])
print(list1[11:14])
print(list1[15:18])

