import cv2


class CursorOverlay:

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def draw(self, frame, landmarks, dragging=False, scrolling=False):

        if landmarks is None:
            return frame

        x = int(landmarks[8][0] * self.width)
        y = int(landmarks[8][1] * self.height)

        color = (0,255,0)

        if dragging:
            color = (0,0,255)

        if scrolling:
            color = (255,0,0)

        cv2.circle(frame, (x,y), 10, color, -1)

        cv2.circle(frame, (x,y), 18, color, 2)

        return frame