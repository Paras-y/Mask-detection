import cv2


import cv2
import numpy as np
net = cv2.dnn.readNet('D:\JUPYTER\object\yolov3_training_last.weights', 'yolov3_testing.cfg')


cnd= cv2.dnn.readNet('D:\\JUPYTER\\object\\yolov3_training_last.weights',config='yolov3_testing.cfg',framework=None)

classes = []
with open("D:\\JUPYTER\\object\\classes (1).txt", "r") as f:
    classes = f.read().splitlines()