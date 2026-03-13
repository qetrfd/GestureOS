import cv2


class SpatialWindow:

    def __init__(self, title, x, y):

        self.title = title

        self.x = x
        self.y = y

        self.w = 250
        self.h = 150

    def draw(self, frame):

        cv2.rectangle(
            frame,
            (self.x, self.y),
            (self.x+self.w, self.y+self.h),
            (50,50,50),
            -1
        )

        cv2.rectangle(
            frame,
            (self.x, self.y),
            (self.x+self.w, self.y+30),
            (90,90,90),
            -1
        )

        cv2.putText(
            frame,
            self.title,
            (self.x+10, self.y+20),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255,255,255),
            2
        )

        return frame

    def move(self, landmarks):

        x = int(landmarks[8][0] * 1280)
        y = int(landmarks[8][1] * 720)

        self.x = x
        self.y = y