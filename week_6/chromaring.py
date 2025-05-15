import numpy as np
import cv2

result_window = 'result'
control_window = 'control'
select_background_color = 'Select BackGround Color'
video_path = 'greenscreen-demo.mp4'
background_path = 'Picture1.jpg'

#Globals
background_color = None
blur = 0
variance = 0
color_spill = 0

#callbacks
def pick_background_color(event, x, y, flags, param):
    global background_color
    if event == cv2.EVENT_LBUTTONDOWN:
        background_color = param[y, x][0]
        print(f"Selected color: {background_color}")

def set_blur(val):
    global blur
    blur = val

def set_variance(val):
    global variance
    variance = val

def set_color_spill(val):
    global color_spill
    color_spill = val

def do_nothing(val):
    pass

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("error opening file")
else:
    background = cv2.imread(background_path)
    ret, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #set up windows
    cv2.namedWindow(result_window)
    cv2.namedWindow(control_window)
    cv2.namedWindow(select_background_color)

    #set up event listeners
    cv2.createTrackbar("variance", control_window, 0, 100, set_variance)
    cv2.createTrackbar("blur", control_window, 0, 100, set_blur)
    cv2.createTrackbar("color cast", control_window, 0, 100, set_color_spill)
    cv2.setMouseCallback(select_background_color, pick_background_color, param=hsv_frame)

    #get background color
    cv2.imshow(select_background_color, frame)
    print("Click on the green screen to select background color and begin or press esc to exit.")
    while background_color is None:
        k = cv2.waitKey(20) & 0xff
        if k == 27:
            break
    cv2.destroyWindow(select_background_color)

    #start video over
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    #resize background image
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    background = cv2.resize(background, (frame_width, frame_height))

    #initialization
    fps = cap.get(cv2.CAP_PROP_FPS)
    wait_time = round(1000 / fps)
    print('wait time', wait_time)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_green = np.array([np.clip(background_color - variance,0, 179), 0, 0])  # HSV lower bound for green
        upper_green = np.array([np.clip(background_color + variance, 0, 179), 255, 255])  # HSV upper bound for green

        mask = cv2.inRange(hsv_frame, lower_green, upper_green)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.erode(mask, kernel, iterations=5)
        mask = cv2.dilate(mask, kernel, iterations=7)
        # cv2.imshow("asdf",mask)
        if blur > 0:
            mask = cv2.GaussianBlur(mask, ((2 * blur) + 1, (2 * blur) + 1), 0)

        frame_copy = frame.copy()
        if color_spill > 0:
            green_spill = np.zeros_like(frame_copy)
            green_spill[:, :, 1] = mask
            frame_copy = cv2.subtract(frame_copy, (green_spill * (color_spill / 100)).astype(np.uint8))

        mask_f = mask.astype(float) / 255.0
        mask_f = cv2.merge([mask_f, mask_f, mask_f])

        alpha_fg = 1.0 - mask_f

        # Convert images to float
        fg_float = frame_copy.astype(float) / 255.0
        bg_float = background.astype(float) / 255.0

        result = fg_float * alpha_fg + bg_float * mask_f
        result = (result * 255).astype(np.uint8)


        # cv2.imshow("mask", mask)
        # cv2.imshow(control, frame)
        cv2.imshow(result_window, result)
        k = cv2.waitKey(wait_time) & 0xff
        if k == 27:
            break




cap.release()
cv2.destroyAllWindows()







