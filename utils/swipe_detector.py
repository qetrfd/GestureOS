class SwipeDetector:

    def __init__(self):

        self.history = []

        self.max_history = 6

    def update(self, landmarks):

        x = landmarks[8][0]

        self.history.append(x)

        if len(self.history) > self.max_history:
            self.history.pop(0)

        if len(self.history) < self.max_history:
            return None

        movement = self.history[-1] - self.history[0]

        if movement > 0.25:
            self.history.clear()
            return "RIGHT"

        if movement < -0.25:
            self.history.clear()
            return "LEFT"

        return None