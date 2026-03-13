import time


class DepthGesture:

    def __init__(self):

        self.history = []
        self.max_history = 6

        self.last_action = 0
        self.cooldown = 0.03

    def update(self, landmarks):

        z = landmarks[8][2]

        self.history.append(z)

        if len(self.history) > self.max_history:
            self.history.pop(0)

        if len(self.history) < self.max_history:
            return None

        movement = self.history[-1] - self.history[0]

        now = time.time()

        if now - self.last_action < self.cooldown:
            return None

        if movement < -0.03:

            self.last_action = now
            return "FORWARD"

        if movement > 0.03:

            self.last_action = now
            return "BACK"

        return None