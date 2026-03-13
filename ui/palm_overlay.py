import cv2


class PalmOverlay:

    def __init__(self, width, height):

        self.width = width
        self.height = height


    def get_palm_center(self, landmarks):

        wrist = landmarks[0]
        index_base = landmarks[5]
        pinky_base = landmarks[17]

        x = (wrist[0] + index_base[0] + pinky_base[0]) / 3
        y = (wrist[1] + index_base[1] + pinky_base[1]) / 3

        return int(x * self.width), int(y * self.height)


    def draw(self, frame, landmarks, fist=False):

        if landmarks is None:
            return frame

        cx, cy = self.get_palm_center(landmarks)

        color = (0,255,0)

        if fist:
            color = (0,0,255)

        cv2.circle(frame, (cx,cy), 12, color, -1)

        cv2.circle(frame, (cx,cy), 24, color, 2)

        return frame