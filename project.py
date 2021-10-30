

from PIL import Image
import os
  

im = Image.open("geeksforgeeks.jpg")
print("The size of the image before conversion : ", end = "")
print(os.path.getsize("geeksforgeeks.jpg"))

rgb_im = im.convert("RGB")
  

rgb_im.save("geeksforgeeks_jpg.jpg")
print("The size of the image after conversion : ", end = "")
print(os.path.getsize("geeksforgeeks_jpg.jpg"))