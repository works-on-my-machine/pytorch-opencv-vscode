from cv2 import cv2
import numpy as np
import os

randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)
grayImage = flatNumpyArray.reshape(300, 400)
cv2.imshow('RandomGray.png', grayImage)
cv2.waitKey()
