# Import libraries
import cv2
import numpy as np
from dataPath import DATA_PATH

#define a global extra alpha to apply
alpha = .5
# Load the Face Image
pathToFace = DATA_PATH + "/images/musk.jpg"
faceImage = cv2.imread(pathToFace)

# Load the Sunglass image with Alpha channel
# (http://pluspng.com/sunglass-png-1104.html)
pathToSunglasses = DATA_PATH + "/images/sunglass.png"
sunglassesPNG = cv2.imread(pathToSunglasses, cv2.IMREAD_UNCHANGED)

# Resize the image to fit over the eye region
sunglassesPNG = cv2.resize(sunglassesPNG,(300,100))
print("image Dimension ={}".format(sunglassesPNG.shape))

# Separate the Color and alpha channels
sunglassBGR = sunglassesPNG[:,:,0:3]
sunglassBGR = sunglassBGR / 255
sunglassMaskAlpha = sunglassesPNG[:,:,3]
sunglassMaskAlpha = (sunglassMaskAlpha / 255) * .5

# Make the dimensions of the mask same as the input image.
# Since Face Image is a 3-channel image, we create a 3 channel image for the mask
sunGlassMask = cv2.merge((sunglassMaskAlpha,sunglassMaskAlpha,sunglassMaskAlpha))

#apply the alpha mask to the sunglasses
sunGlassesWithAlpha = sunglassBGR * sunGlassMask

cv2.imshow("sun glasses alpha",sunGlassMask  )
cv2.imshow("sunglasses", sunGlassesWithAlpha)

# get the eye region of interest
eyeROI = faceImage[150:250,140:440]
eyeROI = eyeROI / 255
cv2.imshow("eye roi", eyeROI)

#apply alpha to eyeroi
eyeROIWithAlpha = (1 - sunGlassMask) * eyeROI
cv2.imshow("eyeroi with alpha", eyeROIWithAlpha)

#add them together
eyesWithGlasses = eyeROIWithAlpha + sunGlassesWithAlpha
cv2.imshow("eyes with glasses", eyesWithGlasses)

faceImage[150:250,140:440] = np.uint8(eyesWithGlasses * 255)
cv2.imshow("result", faceImage)
# # Make the values [0,1] since we are using arithmetic operations
# glassMask = np.uint8(glassMask/255)
#
# # Make a copy
# faceWithGlassesArithmetic = faceImage.copy()
#
# # Get the eye region from the face image
# eyeROI= faceWithGlassesArithmetic[150:250,140:440]
# gm2 = np.where(glassMask == 1, .5, 0)
# # Use the mask to create the masked eye region
# maskedEye = cv2.multiply(eyeROI,(1-  gm2 ))
#
# # Use the mask to create the masked sunglass region
# maskedGlass = cv2.multiply(cv2.multiply(glassBGR, .5),glassMask)
#
# # Combine the Sunglass in the Eye Region to get the augmented image
# eyeRoiFinal = cv2.add(maskedEye, maskedGlass)
#
# cv2.imwrite("results/maskedEyeRegion.png",maskedEye)
# cv2.imwrite("results/maskedSunglassRegion.png",maskedGlass)
# cv2.imwrite("results/augmentedEyeAndSunglass.png",eyeRoiFinal)
#
# # Replace the eye ROI with the output from the previous section
# faceWithGlassesArithmetic[150:250,140:440]=eyeRoiFinal
#
# cv2.imwrite("results/withSunglasses.png",faceWithGlassesArithmetic)
#
# cv2.imshow("Masked Eye Region",maskedEye)
# cv2.imshow("Masked Sunglass Region",maskedGlass)
# cv2.imshow("Augmented Eye and Sunglass",eyeRoiFinal)
# cv2.imshow("With Sunglasses",faceWithGlassesArithmetic)

while True:
    c = cv2.waitKey(20)
    if c == 27:
        break

cv2.destroyAllWindows()