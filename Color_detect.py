import numpy as np
import cv2

# Lower and Upper limit of green color in the format of HSV (H:0-180, S:0-255, V:0-255)
green_lower = np.array([50, 50, 50], dtype=np.uint8)
green_upper = np.array([90, 255, 255], dtype=np.uint8)

# Filter Size to make the detect part run smoother
kernel = np.ones((25, 25), np.uint8)

# Initializing Video Capture #
cap = cv2.VideoCapture(0)

# Accesses camera and finds the targeted color and displays it
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, green_lower, green_upper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    segemented_color = cv2.bitwise_and(frame, frame, mask=mask)
    mask_contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# shows you the results as the computer will see
    results = cv2.drawContours(segemented_color, mask_contours, -1, (0, 0, 255), 3)

# This shows the photo with the box, the mask, and what the computer will see before putting a box this is for debugging
# purposes
  # shows what the camera sees
    #cv2.imshow('Frame', frame)
  # shows what the computer see in HSV
    #cv2.imshow('HSV', hsv)
  # shows what the robot will see
    #cv2.imshow('Mask', mask)
    cv2.imshow('Results', results)

# Waits for the user to hit the q button to close program #
    if cv2.waitKey(1) == ord('q'):
        break

# Allows to release the picture to free used system resources #
cap.release()
cv2.destroyAllWindows()
