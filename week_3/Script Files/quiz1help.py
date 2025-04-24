# Standard imports
import cv2
import numpy as np;
from dataPath import DATA_PATH

# Read image
im1 = cv2.imread(DATA_PATH + "images/quiz1.png", cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread(DATA_PATH + "images/quiz2.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow("1",im1);cv2.imshow("2",im2)

# Set up the detector with default parameters.
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = False
detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(im1)
print(len(keypoints))
keypoints = detector.detect(im2)
print(len(keypoints))
# keypoints = detector.detect(im)

#
#
# # Mark blobs using image annotation concepts we have studied so far
# for k in keypoints:
#     x,y = k.pt
#     x=int(round(x))
#     y=int(round(y))
#     # Mark center in BLACK
#     cv2.circle(im,(x,y),5,(0,0,0),-1)
#     # Get radius of blob
#     diameter = k.size
#     radius = int(round(diameter/2))
#     # Mark blob in RED
#     cv2.circle(im,(x,y),radius,(0,0,255),2)
#
# # Let's see what image we are dealing with
# cv2.imshow("Image",im)

k = 0
# loop until escape character is pressed
while k != 27 :

  k = cv2.waitKey(20) & 0xFF
cv2.destroyAllWindows()
# Setup SimpleBlobDetector parameters.
# params = cv2.SimpleBlobDetector_Params()

# Change thresholds
# params.minThreshold = 10
# params.maxThreshold = 200

# # Filter by Area.
# params.filterByArea = True
# params.minArea = 1500
#
# # Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1
#
# # Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.87
#
# # Filter by Inertia
# params.filterByInertia = True
# params.minInertiaRatio = 0.01
#
# # Create a detector with the parameters
# detector = cv2.SimpleBlobDetector_create(params)
