import time
import cv2


class FPSCounter:

    def __init__(self):
        self.prev_time = 0
        self.curr_time = 0
        self.fps = 0

    def update(self):

        self.curr_time = time.time()

        if self.prev_time != 0:
            self.fps = 1 / (self.curr_time - self.prev_time)

        self.prev_time = self.curr_time

    def draw(self, frame):

        text = f"FPS: {int(self.fps)}"

        cv2.putText(
            frame,
            text,
            (10, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        return frame