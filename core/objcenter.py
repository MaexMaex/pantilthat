import imutils
import cv2

class ObjCenter:
    def __init__(self, haarPath):
        self.detector = cv2.CascadeClassifier(haarPath)
    def update(self, frame, frameCenter):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = self.detector.detectMultiScale(gray, scaleFactor=1.05,
            minNeighbors=9, minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE)
        if len(rects) > 0:
            # extract the bounding box coordinates of the face and
            # use the coordinates to determine the center of the
            # face
            (x, y, w, h) = rects[0]
            faceX = int(x + (w / 2.0))
            faceY = int(y + (h / 2.0))
            # return the center (x, y)-coordinates of the face
            return ((faceX, faceY), rects[0])
        return (frameCenter, None)