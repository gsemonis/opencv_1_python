import cv2

scale = 0
max_scale = 100
scale_type = 0
max_scale_type = 1

window_name = "Resize Image"
trackbar_scale_title = "Scale"
trackbar_type_title = "Type: \n 0: Scale Up \n 1: Scale Down"

# load an image
image = cv2.imread("../data/images/truth.png")

# Create a window to display results
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

def scale_image_function(value):
    global scale
    scale = value
    resize_image()

# Callback functions
def scale_type_function(value):
    global scale_type
    scale_type = value
    resize_image()

def resize_image():
    global scale, scale_type
    scale_factor = 1 + scale / 100.0
    if scale_type == 1:
        scale_factor = 1 / scale_factor

    # Resize the image
    scaled_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(window_name, scaled_image)

cv2.createTrackbar(trackbar_scale_title, window_name, scale, max_scale, scale_image_function)
cv2.createTrackbar(trackbar_type_title, window_name, scale_type, max_scale_type, scale_type_function)

cv2.imshow(window_name, image)
c = cv2.waitKey(0)

cv2.destroyAllWindows()