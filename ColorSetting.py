import numpy as np
import cv2


class Color:
    def __init__(self):
        super().__init__()
        # Setting the features of the color detection
        self.lowerLimit = []
        self.higherLimit = []
        self.lowerLimitRed = []
        self.higherLimitRed = []
        self.colorInput = None
        self.mask = None
        self.maskRed = None

    def color_detect(self, gui_color, hsv):
        # Takes GUI software's choice and changes Limits for color detection
        self.colorInput = gui_color
        if gui_color == 'Yellow':
            self.lowerLimit = np.array([20, 50, 50], dtype=np.uint8)
            self.higherLimit = np.array([50, 255, 255], dtype=np.uint8)
            self.mask = cv2.inRange(hsv, self.lowerLimit, self.higherLimit)
        elif gui_color == 'Red':
            self.lowerLimit = np.array([0, 150, 150], dtype=np.uint8)
            self.higherLimit = np.array([10, 255, 255], dtype=np.uint8)
            self.lowerLimitRed = np.array([170, 150, 150], dtype=np.uint8)
            self.higherLimitRed = np.array([180, 255, 255], dtype=np.uint8)
            self.mask = cv2.inRange(hsv, self.lowerLimit, self.higherLimit)
            self.maskRed = cv2.inRange(hsv, self.lowerLimitRed, self.higherLimitRed)
            self.mask = self.mask + self.maskRed
        elif gui_color == 'Blue':
            self.lowerLimit = np.array([100, 100, 100], dtype=np.uint8)
            self.higherLimit = np.array([130, 255, 255], dtype=np.uint8)
            self.mask = cv2.inRange(hsv, self.lowerLimit, self.higherLimit)
        elif gui_color == 'Green':
            self.lowerLimit = np.array([50, 50, 50], dtype=np.uint8)
            self.higherLimit = np.array([90, 255, 255], dtype=np.uint8)
            self.mask = cv2.inRange(hsv, self.lowerLimit, self.higherLimit)
        return self.mask
