import cv2
import numpy as np
import math

a = cv2.imread('D:/DL/Kaggle-Steel-Defect-Detection-master/datasets/Steel_data/train_images/5bdeb5f66.jpg')
print(type(a))
b = cv2.imread('./image/5bdeb5f66.jpg')
cv2.imshow('Image', b)
cv2.waitKey(0)
cv2.destroyAllWindows()