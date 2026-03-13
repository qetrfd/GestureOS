import math
import pyautogui


class TwoHandZoom:

    def __init__(self):

        self.prev_distance = None

        self.zoom_sensitivity = 0.015

    def update(self, hands):

        if len(hands) < 2:
            self.prev_distance = None
            return

        p1 = hands[0][8]
        p2 = hands[1][8]

        dx = p1[0] - p2[0]
        dy = p1[1] - p2[1]

        distance = math.sqrt(dx*dx + dy*dy)

        if self.prev_distance is None:

            self.prev_distance = distance
            return

        delta = distance - self.prev_distance

        if delta > self.zoom_sensitivity:

            print("Zoom In")

            pyautogui.scroll(120)

        elif delta < -self.zoom_sensitivity:

            print("Zoom Out")

            pyautogui.scroll(-120)

        self.prev_distance = distance