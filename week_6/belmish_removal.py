import cv2
import numpy as np

def remove_blemish(action, x, y, flags, userdata):
  global blemish_image, previous_images, patch_size

  # left button down
  if action == cv2.EVENT_LBUTTONDOWN:
    if patch_size % 2 == 0:
      patch_size += 1

    previous_images.append(blemish_image.copy())
    grey = cv2.cvtColor(blemish_image, cv2.COLOR_BGR2GRAY)

    # for space for patches around the click
    half_patch_size = patch_size // 2

    #find the corners of roi
    max_y, max_x = grey.shape
    min_roi_x = max(0, x - half_patch_size)
    min_roi_y = max(0, y - half_patch_size)
    max_roi_x = min(max_x, x + half_patch_size + 1)
    max_roi_y = min(max_y, y + half_patch_size + 1)

    #size of actual patch
    roi = grey[min_roi_y : max_roi_y, min_roi_x : max_roi_x]
    actual_patch_height, actual_patch_width = roi.shape

    #define the search area
    min_search_area_x = max(0, min_roi_x - actual_patch_width)
    min_search_area_y = max(0, min_roi_y - actual_patch_height)
    max_search_area_x = min(max_x, max_roi_x + actual_patch_width)
    max_search_area_y = min(max_y, max_roi_y + actual_patch_height)
    search_area = grey[min_search_area_y : max_search_area_y, min_search_area_x : max_search_area_x]

    #find smoothest area
    variance = float("inf")
    left = 0
    top = 0
    for i in range(min_search_area_y, max_search_area_y - actual_patch_height):
      for j in range(min_search_area_x, max_search_area_x - actual_patch_width):
        current_area = grey[i : i + actual_patch_height, j : j + actual_patch_width]
        patch_variance =  np.var(cv2.Laplacian(current_area, cv2.CV_64F))
        if patch_variance < variance:
          variance = patch_variance
          top = i
          left = j

    #get smoothest area
    smoothest_area = blemish_image[top: top + actual_patch_height, left : left + actual_patch_width]
    mask = np.ones_like(smoothest_area, smoothest_area.dtype)
    mask *= 255
    blemish_image = cv2.seamlessClone(smoothest_area, blemish_image, mask, (x,y), cv2.NORMAL_CLONE)

    cv2.imshow("blemish", blemish_image)
    # cv2.imshow("smooth",smoothest_area)
  if action == cv2.EVENT_RBUTTONDOWN:
    if len(previous_images) > 0:
      blemish = previous_images.pop()
      cv2.imshow("blemish", blemish)

patch_size = 30
previous_images = []

cv2.namedWindow("blemish")
# cv2.namedWindow("smooth")
blemish_image = cv2.imread("blemish.png", cv2.IMREAD_COLOR)

cv2.setMouseCallback("blemish", remove_blemish)

cv2.imshow("blemish", blemish_image)

k = 0
# loop until escape character is pressed
while k != 27 :
  k = cv2.waitKey(20) & 0xFF
cv2.destroyAllWindows()
