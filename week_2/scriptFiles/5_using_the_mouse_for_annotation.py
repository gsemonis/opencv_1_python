import cv2
import numpy as np
import math

# Lists to store the points
down_point = (-1, -1)
up_point = (-1,1)
drawing = False

def draw_rectangle(action, x, y, flags, userdata):

  global down_point, up_point, drawing, source, source_copy, over_lay

  # left button down
  if action == cv2.EVENT_LBUTTONDOWN:
    drawing = True
    down_point = (x,y)
    up_point = (x,y)

  elif action == cv2.EVENT_MOUSEMOVE:
    if drawing:
      up_point = (x,y)
      over_lay = np.zeros_like(source)
      cv2.rectangle(over_lay, down_point, up_point, (255,0,255), 3, lineType = cv2.LINE_AA)
      source_copy = cv2.add(source, over_lay)
      cv2.imshow("Window", source_copy)

  # left button up
  elif action==cv2.EVENT_LBUTTONUP:
    drawing = False
    up_point = (x,y)
    cv2.rectangle(over_lay, down_point, up_point,(255,0,255), 3, cv2.LINE_AA)
    source_copy = cv2.add(source, over_lay)
    cv2.imshow("Window", source_copy)

    x1, y1 = down_point
    x2, y2 = up_point

    x_min, x_max = sorted([x1, x2])
    y_min, y_max = sorted([y1, y2])

    crop_area = source_copy[y_min:y_max, x_min:x_max]
    cv2.imwrite("croppedArea.jpg", crop_area)
    #cv2.imshow("cropped area", crop_area)



source = cv2.imread("../data/images/sample.jpg", cv2.IMREAD_COLOR)
cv2.putText(source, '''Choose corner, and drag, Press ESC to exit and c to clear''', (10, 30),
              cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
source_copy = source.copy()

#make an overlay for drawing on
over_lay = np.zeros_like(source)

cv2.namedWindow("Window")

# highgui function called when mouse events occur
cv2.setMouseCallback("Window", draw_rectangle)
k = 0
# loop until escape character is pressed
while k != 27 :
  cv2.imshow("Window", source_copy)

  k = cv2.waitKey(20) & 0xFF
  if k==99:
    over_lay = np.zeros_like(source)
    source_copy = source.copy()

cv2.destroyAllWindows()
