import numpy as np
import cv2

class Freehand:
    width = 800
    height = 1000
    x = 0
    y = 0
    drawing = False

    def __init__(self):
        self.box = np.zeros((self.width, self.height, 1), np.uint8)
        self.box.fill(255)
    
    def run(self):
        global x, y, drawing

        def draw(event, current_x, current_y, flags, params):
            if event == cv2.EVENT_LBUTTONDOWN:
                self.x = current_x
                self.y = current_y
                self.drawing = True

            elif event == cv2.EVENT_MOUSEMOVE:
                if self.drawing:
                    cv2.line(self.box, (current_x, current_y), (self.x, self.y), 0, thickness=3)
                    self.x, self.y = current_x, current_y
            
            elif event == cv2.EVENT_LBUTTONUP:
                self.drawing = False
        
        cv2.imshow('draw', self.box)
        cv2.setMouseCallback('draw', draw)

        while True:
            cv2.imshow('draw', self.box)
            if cv2.waitKey(1) & 0xFF == 27:
                return self.box

    def save(self, path):
        cv2.imwrite(path, self.box)
