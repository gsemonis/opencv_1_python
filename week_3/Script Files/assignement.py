import cv2
import numpy as np
from dataPath import DATA_PATH
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

im = np.zeros((10,10),dtype='uint8')

im[0,1] = 1
im[-1,0]= 1
im[-2,-1]=1
im[2,2] = 1
im[5:8,5:8] = 1

element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
ksize = element.shape[0]
height,width = im.shape[:2]

dilatedEllipseKernel = cv2.dilate(im, element)

border = ksize // 2
paddedIm = np.zeros((height + border * 2, width + border * 2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value=0)
paddedDilatedIm = paddedIm.copy()

# Create a VideoWriter object
# Use frame size as 50x50
###
### YOUR CODE HERE
###
videoWriter = cv2.VideoWriter('dilationScratch.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))

for h_i in range(border, height + border):
    for w_i in range(border, width + border):
        ###
        ### YOUR CODE HERE
        ###
        roi = paddedIm[h_i - border: h_i + border + 1, w_i - border: w_i + border + 1]
        roi_and_element = np.bitwise_and(roi, element)

        paddedDilatedIm[h_i, w_i] = 1 if np.any(roi_and_element) else 0

        # Resize output to 50x50 before writing it to the video
        ###
        ### YOUR CODE HERE
        ###
        paddingRemoved = paddedDilatedIm[border:-border, border:-border]
        resized = cv2.resize(paddingRemoved, (50, 50), interpolation=cv2.INTER_NEAREST)

        # Convert resizedFrame to BGR before writing
        ###
        ### YOUR CODE HERE
        ###
        resized *= 255
        bgr = cv2.cvtColor(resized, cv2.COLOR_GRAY2BGR)

        videoWriter.write(bgr)

# Release the VideoWriter object
###
### YOUR CODE HERE
###
videoWriter.release()

border = ksize // 2
paddedIm = np.zeros((height + border * 2, width + border * 2))
paddedIm = cv2.copyMakeBorder(im, border, border, border, border, cv2.BORDER_CONSTANT, value=1)
paddedErodedIm = paddedIm.copy()

# Create a VideoWriter object
# Use frame size as 50x50
###
### YOUR CODE HERE
###
videoWriter = cv2.VideoWriter('erosionScratch.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (50, 50))
for h_i in range(border, height + border):
    for w_i in range(border, width + border):
        ###
        ### YOUR CODE HERE
        ###
        roi = paddedIm[h_i - border: h_i + border + 1, w_i - border: w_i + border + 1]
        roi = roi[element == 1]

        paddedErodedIm[h_i, w_i] = 1 if np.all(roi) else 0

        # Resize output to 50x50 before writing it to the video
        ###
        ### YOUR CODE HERE
        ###
        paddingRemoved = paddedErodedIm[border:-border, border:-border]
        resized = cv2.resize(paddingRemoved, (50, 50), interpolation=cv2.INTER_NEAREST)

        # Convert resizedFrame to BGR before writing
        ###
        ### YOUR CODE HERE
        ###
        resized *= 255
        bgr = cv2.cvtColor(resized, cv2.COLOR_GRAY2BGR)

        videoWriter.write(bgr)
# Release the VideoWriter object
###
### YOUR CODE HERE
###
videoWriter.release()