import cv2
import numpy as np
import matplotlib.pyplot as plt
def show(img,sbg,swbg):
  plt.figure(figsize=(12,10))
  plt.subplot(1,3,1)
  plt.imshow(img,cmap='gray')
  plt.title('Original')
  plt.subplot(1,3,2)
  plt.imshow(sbg,cmap='gray')
  plt.title('Slice With BG')
  plt.subplot(1,3,3)
  plt.imshow(swbg,cmap='gray')
  plt.title('Slice Without BG')
  plt.tight_layout()
  plt.show()
rmin=100
rmax=200
img=cv2.imread('monalisa.jpg',0)
if img is None:
  print("IMg NOt Found")
else:
  slice_with_bg=img.copy()
  slice_without_bg=np.zeros(img.shape,dtype=np.uint8)
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      pixel_value=img[i][j]
      if rmin<=pixel_value<=rmax:
        slice_with_bg[i][j]=255
        slice_without_bg[i][j]=255
      else:
        slice_without_bg[i][j]=0
  show(img,slice_with_bg,slice_without_bg)