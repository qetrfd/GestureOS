import math
import time


class RotationGesture:

    def __init__(self):

        self.prev_angle = None

        self.last_trigger = 0

        self.cooldown = 0.25

        self.threshold = 0.35

    def get_angle(self, hand):

        wrist = hand[0]
        middle_base = hand[9]

        dx = middle_base[0] - wrist[0]
        dy = middle_base[1] - wrist[1]

        angle = math.atan2(dy, dx)

        return angle

    def update(self, hand):

        angle = self.get_angle(hand)

        if self.prev_angle is None:

            self.prev_angle = angle
            return None

        diff = angle - self.prev_angle

        self.prev_angle = angle

        now = time.time()

        if now - self.last_trigger < self.cooldown:
            return None

        if diff > self.threshold:

            self.last_trigger = now
            return "ROTATE_RIGHT"

        if diff < -self.threshold:

            self.last_trigger = now
            return "ROTATE_LEFT"

        return None