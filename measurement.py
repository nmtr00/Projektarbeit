import cv2
import numpy as np


##############################

webcam = False
path = '1.jpg'
cap = cv2.VideoCapture(0)

cap.set(10,160) ##Seting for brightness
cap.set(3, 1920)  #Width
cap.set(4, 1080)  #Height


while True:
    if success,img = cap.read()
    else: img = cv2.imread(path)
    cv2.imshow('Original', img)
    cv2.waitKey(1)
