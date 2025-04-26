#!/usr/bin/env python
# coding: utf-8

# # <font style = "color:rgb(50,120,229)"> Coin Detection </font>
# 
# So far we have studied about various mophological operations and different thresholding techniques in some detail. Now it's time to apply these concepts for a practical application - **Coin Detection**.
# 
# ## <font style = "color:rgb(50,120,229)"> Aim </font>
# 
# In this assignment, you will work with 2 different images (so 2 different parts) and will use **only** morphological operations and thresholding techniques to detect the total number of coins present in the image. Your submission will be graded based on your use of the concepts covered in this module, experimentation performed to achieve at your final solution, documentation, and finally, the total number of coins successfully detected in the images. Each part will be of 15 marks. This assignment will be entirely **manually graded** so make sure that you do NOT remove any experimentation you have done as well as the observation you made after each step.
# 
# **Proper documentation for each step should be provided with help of markdown**
# 
# ## <font style = "color:rgb(50,120,229)">Outline</font>
# 
# The main steps that you can follow to solve this assignment are:
# 
# 1. Read the image.
# 2. Convert it to grayscale and split the image into the 3 (Red, Green and Blue) channels. Decide which of the above 4 images you want to use in further steps and provide reason for the same.
# 3. Use thresholding and/or morphological operations to arrive at a final binary image.
# 4. Use **simple blob detector** to count the number of coins present in the image.
# 5. Use **contour detection** to count the number of coins present in the image.
# 6. Use **CCA** to count the number of coins present in the image.
# 
# **We have also provided the results we obtained at the intermediate steps for your reference.**

# # <font style = "color:rgb(50,120,229)">Assignment Part - A</font>

# ## <font style = "color:rgb(50,120,229)"> Step 1: Read Image</font>

# In[140]:


import cv2
import matplotlib.pyplot as plt
import numpy as np
# In[141]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = (10.0, 10.0)
matplotlib.rcParams['image.cmap'] = 'gray'


# In[142]:


# Image path
imagePath = "CoinsA.png"
# Read image
# Store it in the variable image
###
### YOUR CODE HERE
###
image =  cv2.imread(imagePath, cv2.IMREAD_COLOR)
imageCopy = image.copy()
# plt.imshow(image[:,:,::-1])
# plt.title("Original Image")
# plt.show()


# ## <font style = "color:rgb(50,120,229)">Step 2.1: Convert Image to Grayscale</font>

# In[143]:


# Convert image to grayscale
# Store it in the variable imageGray
###
### YOUR CODE HERE
###
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# In[144]:


# plt.figure(figsize=(12,12))
# plt.subplot(121)
# plt.imshow(image[:,:,::-1])
# plt.title("Original Image")
# plt.subplot(122)
# plt.imshow(imageGray)
# plt.title("Grayscale Image")
# plt.show()


# ## <font style = "color:rgb(50,120,229)">Step 2.2: Split Image into R,G,B Channels</font>

# In[145]:


# Split cell into channels
# Store them in variables imageB, imageG, imageR
###
### YOUR CODE HERE
###
imageB, imageG, imageR = cv2.split(image)

# In[146]:


# plt.figure(figsize=(20,12))
# plt.subplot(141)
# plt.imshow(image[:,:,::-1])
# plt.title("Original Image")
# plt.subplot(142)
# plt.imshow(imageB)
# plt.title("Blue Channel")
# plt.subplot(143)
# plt.imshow(imageG)
# plt.title("Green Channel")
# plt.subplot(144)
# plt.imshow(imageR);
# plt.title("Red Channel")
# plt.show()

# ## <font style = "color:rgb(50,120,229)">Step 3.1: Perform Thresholding</font>
# 
# You will have to carry out this step with different threshold values to see which one suits you the most. Do not remove those intermediate images and make sure to document your findings.

# In[147]:


###
### YOUR CODE HERE
###
_, thresh = cv2.threshold(imageG, 15, 255, cv2.THRESH_BINARY_INV)



# In[148]:


# Display the thresholded image
###
### YOUR CODE HERE
###
# plt.title("threshold image")
# plt.imshow(thresh)
# plt.show()

# ## <font style = "color:rgb(50,120,229)">Step 3.2: Perform morphological operations</font>
# 
# You will have to carry out this step with different kernel size, kernel shape and morphological operations to see which one (or more) suits you the most. Do not remove those intermediate images and make sure to document your findings.

# In[149]:


###
### YOUR CODE HERE
###
element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (6,6))
imageMorphOpened = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, element, iterations=3)
# plt.title("closed image")
# plt.imshow(imageMorphOpened)
# plt.show()
# In[150]:


###
### YOUR CODE HERE
###


# In[151]:


# Display all the images
# you have obtained in the intermediate steps
###
### YOUR CODE HERE
###


# In[152]:


# Get structuring element/kernel which will be used for dilation
###
### YOUR CODE HERE
###


# In[153]:


###
### YOUR CODE HERE
###


# In[154]:


###
### YOUR CODE HERE
###


# ## <font style = "color:rgb(50,120,229)">Step 4.1: Create SimpleBlobDetector</font>

# In[155]:


# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()

params.blobColor = 0

params.minDistBetweenBlobs = 2

# Filter by Area.
params.filterByArea = False

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.8

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.8

# Filter by Inertia
params.filterByInertia =True
params.minInertiaRatio = 0.8


# In[156]:


# Create SimpleBlobDetector
detector = cv2.SimpleBlobDetector_create(params)


# ## <font style = "color:rgb(50,120,229)">Step 4.2: Detect Coins</font>
# 
# ### <font style = "color:rgb(8,133,37)">Hints</font>
# Use **`detector.detect(image)`** to detect the blobs (coins). The output of the function is a list of **keypoints** where each keypoint is unique for each blob.
# 
# Print the number of coins detected as well.

# In[157]:


# Detect blobs
###
### YOUR CODE HERE
###
keypoints = detector.detect(imageMorphOpened)

# In[158]:


# Print number of coins detected
###
### YOUR CODE HERE
###

print("coins detected = {}".format(len(keypoints)))
# **Note that we were able to detect all 9 coins. So, that's your benchmark.**

# ## <font style = "color:rgb(50,120,229)">Step 4.3: Display the detected coins on original image</font>
# 
# Make sure to mark the center of the blobs as well. **Use only the functions discussed in Image Annotation section in Week 1**
# 
# ### <font style = "color:rgb(8,133,37)">Hints</font>
# You can extract the coordinates of the center and the diameter of a blob using **`k.pt`** and **`k.size`** where `k` is a keypoint.

# In[159]:


# Mark coins using image annotation concepts we have studied so far
###
### YOUR CODE HERE
###

image_copy2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
for point in keypoints:
    x,y = point.pt
    x = int(round(x))
    y = int(round(y))
    cv2.circle(image_copy2, (x,y), 3, (255,0,0), -1)
    cv2.circle(image_copy2, (x,y), int(point.size // 2), (0,0,255), 3)

# In[160]:


# Display the final image
###
### YOUR CODE HERE
###
# plt.title("blobs")
# plt.imshow(image_copy2)
# plt.show()

# ## <font style = "color:rgb(50,120,229)">Step 4.4: Perform Connected Component Analysis</font>
# 
# In the final step, perform Connected Component Analysis (CCA) on the binary image to find out the number of connected components. Do you think we can use CCA to calculate number of coins? Why/why not?

# In[161]:


def displayConnectedComponents(im):
    imLabels = im
    # The following line finds the min and max pixel values
    # and their locations in an image.
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(imLabels)
    # Normalize the image so the min value is 0 and max value is 255.
    imLabels = 255 * (imLabels - minVal)/(maxVal-minVal)
    # Convert image to 8-bits unsigned type
    imLabels = np.uint8(imLabels)
    # Apply a color map
    imColorMap = cv2.applyColorMap(imLabels, cv2.COLORMAP_JET)
    # Display colormapped labels
    plt.imshow(imColorMap[:,:,::-1])


# In[162]:


# Find connected components
###
### YOUR CODE HERE
###
#
_, imageMorphOpened = cv2.threshold(imageMorphOpened, 50, 255, cv2.THRESH_BINARY_INV)
label_count, imLabels = cv2.connectedComponents(imageMorphOpened)
# plt.imshow(imLabels)
# plt.show()
# In[163]:


# Print number of connected components detected
###
### YOUR CODE HERE
###
print("number of connected components = {} including the background. {} without the background".format(label_count, label_count - 1))

# In[164]:


# Display connected components using displayConnectedComponents
# function
###
### YOUR CODE HERE
###
# displayConnectedComponents(imLabels)
# plt.show()

# ## <font style = "color:rgb(50,120,229)">Step 4.5: Detect coins using Contour Detection</font>
# 
# In the final step, perform Contour Detection on the binary image to find out the number of coins.

# In[165]:


# Find all contours in the image
###
### YOUR CODE HERE
###
contours, hierarchy = cv2.findContours(imageMorphOpened, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE )

# In[166]:


# Print the number of contours found
###
### YOUR CODE HERE
###
print("Number of contours = {}".format(len(contours)))

# In[167]:


# Draw all contours
###
### YOUR CODE HERE
###
image_copy = image.copy()
contoursImage = cv2.drawContours(image_copy, contours, -1, (255,0,255), 3)
plt.title("contours with coins")
# plt.imshow(contoursImage[:,:,::-1])
# plt.show()
# Let's only consider the outer contours.

# In[168]:


# Remove the inner contours
# Display the result
###
### YOUR CODE HERE
###
contours, hierarchy = cv2.findContours(imageMorphOpened, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE )
print("Number of contours = {}".format(len(contours)))
# So, we only need the inner contours. The easiest way to do that will be to remove the outer contour using area.

# In[169]:


# Print area and perimeter of all contours
###
### YOUR CODE HERE
###
for index,cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    perimeter = cv2.arcLength(cnt, True)
    print("Contour #{} has area = {} and perimeter = {}".format(index+1,area,perimeter))

# In[170]:


# Print maximum area of contour
# This will be the box that we want to remove
###
### YOUR CODE HERE
###
largest_contour = max(contours, key=cv2.contourArea)
print("largest contour area = {} ".format(cv2.contourArea(largest_contour)))
# In[171]:


# Remove this contour and plot others
###
### YOUR CODE HERE
###
image_copy = image.copy()
filtered_contours = [cnt for cnt in contours if not (cnt is largest_contour)]
contoursImage2 = cv2.drawContours(image_copy, filtered_contours, -1, (255,0,255), 3)
# plt.imshow(contoursImage2[:,:,::-1])
# plt.show()
# In[173]:


# Fit circles on coins
###
### YOUR CODE HERE
###
image_copy = image.copy()
for cnt in contours:
    # Fit a circle
    ((x,y),radius) = cv2.minEnclosingCircle(cnt)
    cv2.circle(image, (int(x),int(y)), int(round(radius)), (0,255,255), 2)
# plt.imshow(image[:,:,::-1])

# # <font style = "color:rgb(50,120,229)">Assignment Part - B</font>
# 
# **Follow the same steps as provided in Assignment Part - A**

# ## <font style = "color:rgb(50,120,229)"> Step 1: Read Image</font>

# In[30]:


# Image path
imagePath = "CoinsB.png"
# Read image
# Store it in variable image
###
### YOUR CODE HERE
###
image =  cv2.imread(imagePath, cv2.IMREAD_COLOR)
image_copy = image.copy()
plt.imshow(image[:,:,::-1]);
plt.title("Original Image")
plt.show()

# ## <font style = "color:rgb(50,120,229)">Step 2.1: Convert Image to Grayscale</font>

# In[31]:


# Convert to grayscale
# Store in variable imageGray
###
### YOUR CODE HERE
###


# In[32]:


plt.figure(figsize=(12,12))
plt.subplot(121)
plt.imshow(image[:,:,::-1]);
plt.title("Original Image")
plt.subplot(122)
plt.imshow(imageGray);
plt.title("Grayscale Image");


# ## <font style = "color:rgb(50,120,229)">Step 2.2: Split Image into R,G,B Channels</font>

# In[33]:


# Split cell into channels
# Variables are: imageB, imageG, imageR
###
### YOUR CODE HERE
###


# In[34]:


plt.figure(figsize=(20,12))
plt.subplot(141)
plt.imshow(image[:,:,::-1]);
plt.title("Original Image")
plt.subplot(142)
plt.imshow(imageB);
plt.title("Blue Channel")
plt.subplot(143)
plt.imshow(imageG);
plt.title("Green Channel")
plt.subplot(144)
plt.imshow(imageR);
plt.title("Red Channel");


# ## <font style = "color:rgb(50,120,229)">Step 3.1: Perform Thresholding</font>
# 
# You will have to carry out this step with different threshold values to see which one suits you the most. Do not remove those intermediate images and make sure to document your findings.

# In[35]:


###
### YOUR CODE HERE
###


# In[36]:


# Display image using matplotlib
###
### YOUR CODE HERE
###


# ## <font style = "color:rgb(50,120,229)">Step 3.2: Perform morphological operations</font>
# 
# You will have to carry out this step with different kernel size, kernel shape and morphological operations to see which one (or more) suits you the most. Do not remove those intermediate images and make sure to document your findings.

# In[37]:


###
### YOUR CODE HERE
###


# In[38]:


###
### YOUR CODE HERE
###


# In[39]:


###
### YOUR CODE HERE
###


# In[40]:


###
### YOUR CODE HERE
###


# In[41]:


###
### YOUR CODE HERE
###


# In[42]:


###
### YOUR CODE HERE
###


# In[43]:


###
### YOUR CODE HERE
###


# In[44]:


###
### YOUR CODE HERE
###


# In[45]:


###
### YOUR CODE HERE
###


# In[46]:


###
### YOUR CODE HERE
###


# In[47]:


###
### YOUR CODE HERE
###


# In[48]:


###
### YOUR CODE HERE
###


# In[49]:


###
### YOUR CODE HERE
###


# In[50]:


###
### YOUR CODE HERE
###


# In[51]:


###
### YOUR CODE HERE
###


# In[52]:


###
### YOUR CODE HERE
###


# In[53]:


###
### YOUR CODE HERE
###


# ## <font style = "color:rgb(50,120,229)">Step 4.1: Create SimpleBlobDetector</font>

# In[54]:


# Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()

params.blobColor = 0

params.minDistBetweenBlobs = 2

# Filter by Area.
params.filterByArea = False

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.8

# Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.8

# Filter by Inertia
params.filterByInertia =True
params.minInertiaRatio = 0.8


# In[55]:


# Create SimpleBlobDetector
detector = cv2.SimpleBlobDetector_create(params)


# 
# ## <font style = "color:rgb(50,120,229)">Step 4.2: Detect Coins</font>
# 
# ### <font style = "color:rgb(8,133,37)">Hints</font>
# Use **`detector.detect(image)`** to detect the blobs (coins). The output of the function is a list of **keypoints** where each keypoint is unique for each blob.
# 
# Print the number of coins detected as well.

# In[56]:


# Detect blobs
###
### YOUR CODE HERE
###


# ## <font style = "color:rgb(50,120,229)">Step 4.3: Display the detected coins on original image</font>
# 
# Make sure to mark the center of the blobs as well. **Use only the functions discussed in Image Annotation section in Week 1**
# 
# ### <font style = "color:rgb(8,133,37)">Hints</font>
# You can extract the coordinates of the center and the diameter of a blob using **`k.pt`** and **`k.size`** where `k` is a keypoint.

# In[57]:


###
### YOUR CODE HERE
###


# In[58]:


###
### YOUR CODE HERE
###


# In[59]:


###
### YOUR CODE HERE
###


# **Note that we were able to detect 8 coins. So, that's your benchmark.**

# ## <font style = "color:rgb(50,120,229)">Step 4.4: Perform Connected Component Analysis</font>
# 
# Now, let's perform Connected Component Analysis (CCA) on the binary image to find out the number of connected components. Do you think we can use CCA to calculate number of coins? Why/why not?

# In[60]:


###
### YOUR CODE HERE
###


# In[61]:


###
### YOUR CODE HERE
###


# In[62]:


###
### YOUR CODE HERE
###


# ## <font style = "color:rgb(50,120,229)">Step 4.5: Detect coins using Contour Detection</font>
# 
# In the final step, perform Contour Detection on the binary image to find out the number of coins.

# In[63]:


# Find all contours in the image
###
### YOUR CODE HERE
###


# In[64]:


# Print the number of contours found
###
### YOUR CODE HERE
###


# In[65]:


# Draw all contours
###
### YOUR CODE HERE
###


# In[66]:


# Remove the inner contours
# Display the result
###
### YOUR CODE HERE
###


# What do you think went wrong? As we can see, the outer box was detected as a contour and with respect to it, all other contours are internal and that's why they were not detected. How do we remove that? Let's see if we can use area of contours here.

# In[67]:


# Print area and perimeter of all contours
###
### YOUR CODE HERE
###


# In[68]:


# Print maximum area of contour
# This will be the box that we want to remove
###
### YOUR CODE HERE
###


# In[69]:


# Remove this contour and plot others
###
### YOUR CODE HERE
###


# Now, we have to remove the internal contours. Again here we can use area or perimeter.

# In[70]:


# Print sorted area of contours
###
### YOUR CODE HERE
###


# We can clearly see the jump from 2nd area to 3rd. These are the 2 inner contours.

# In[71]:


# Remove the 2 inner contours
# Plot the rest of them
###
### YOUR CODE HERE
###


# In[72]:


# Fit circles on coins
###
### YOUR CODE HERE
###

