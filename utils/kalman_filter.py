import cv2
import numpy as np


class Kalman2D:

    def __init__(self):

        self.kalman = cv2.KalmanFilter(4, 2)

        self.kalman.measurementMatrix = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0]
        ], np.float32)

        self.kalman.transitionMatrix = np.array([
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ], np.float32)

        self.kalman.processNoiseCov = np.eye(4, dtype=np.float32) * 0.03

        self.initialized = False

    def update(self, x, y):

        measurement = np.array([[np.float32(x)], [np.float32(y)]])

        if not self.initialized:

            self.kalman.statePre = np.array([[x], [y], [0], [0]], np.float32)
            self.kalman.statePost = np.array([[x], [y], [0], [0]], np.float32)

            self.initialized = True

        self.kalman.correct(measurement)

        prediction = self.kalman.predict()

        return int(prediction[0]), int(prediction[1])