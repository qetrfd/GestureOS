import cv2


class Camera:

    def __init__(self, width=640, height=480):

        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        self.cap.set(cv2.CAP_PROP_FPS, 60)

        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def get_frame(self):

        ret, frame = self.cap.read()

        if not ret:
            return None

        frame = cv2.flip(frame, 1)

        return frame

    def release(self):

        self.cap.release()