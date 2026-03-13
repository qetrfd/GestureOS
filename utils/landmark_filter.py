class LandmarkFilter:

    def __init__(self):

        self.prev = None

        self.alpha = 0.6

    def apply(self, landmarks):

        if self.prev is None:

            self.prev = landmarks

            return landmarks

        filtered = []

        for p, c in zip(self.prev, landmarks):

            x = p[0] + (c[0] - p[0]) * self.alpha
            y = p[1] + (c[1] - p[1]) * self.alpha
            z = p[2] + (c[2] - p[2]) * self.alpha

            filtered.append((x, y, z))

        self.prev = filtered

        return filtered