import pyautogui
import math
import time


class MouseControl:

    def __init__(self):

        self.screen_w, self.screen_h = pyautogui.size()

        self.prev_x = None
        self.prev_y = None

        self.cursor_speed = 1.8
        self.smooth = 3

        self.dragging = False

        self.last_click = 0

        self.prev_scroll_y = None

        self.prev_fist = False


    def move(self, landmarks):

        x = landmarks[8][0]
        y = landmarks[8][1]

        screen_x = int(x * self.screen_w)
        screen_y = int(y * self.screen_h)

        if self.prev_x is None:

            self.prev_x = screen_x
            self.prev_y = screen_y

        dx = screen_x - self.prev_x
        dy = screen_y - self.prev_y

        screen_x = self.prev_x + dx * self.cursor_speed
        screen_y = self.prev_y + dy * self.cursor_speed

        curr_x = self.prev_x + (screen_x - self.prev_x) / self.smooth
        curr_y = self.prev_y + (screen_y - self.prev_y) / self.smooth

        pyautogui.moveTo(curr_x, curr_y)

        self.prev_x = curr_x
        self.prev_y = curr_y


    def pinch_distance(self, landmarks):

        thumb = landmarks[4]
        index = landmarks[8]

        return math.sqrt(
            (thumb[0]-index[0])**2 +
            (thumb[1]-index[1])**2
        )


    def two_finger_distance(self, landmarks):

        index = landmarks[8]
        middle = landmarks[12]

        return math.sqrt(
            (index[0]-middle[0])**2 +
            (index[1]-middle[1])**2
        )


    def is_fist(self, landmarks):

        tips = [8,12,16,20]
        bases = [5,9,13,17]

        closed = 0

        for tip, base in zip(tips, bases):

            if landmarks[tip][1] > landmarks[base][1]:
                closed += 1

        thumb_closed = abs(landmarks[4][0] - landmarks[3][0]) < 0.05

        return closed >= 3 and thumb_closed


    def click(self, landmarks):

        fist = self.is_fist(landmarks)

        if fist and not self.prev_fist:

            now = time.time()

            if now - self.last_click > 0.4:

                pyautogui.click()

                self.last_click = now

        self.prev_fist = fist


    def drag(self, landmarks):

        dist = self.pinch_distance(landmarks)

        pinch_threshold = 0.035

        if dist < pinch_threshold:

            if not self.dragging:

                pyautogui.mouseDown()

                self.dragging = True

        else:

            if self.dragging:

                pyautogui.mouseUp()

                self.dragging = False


    def scroll(self, landmarks):

        dist = self.two_finger_distance(landmarks)

        scroll_threshold = 0.04

        if dist < scroll_threshold:

            y = landmarks[8][1]

            if self.prev_scroll_y is None:

                self.prev_scroll_y = y
                return

            dy = y - self.prev_scroll_y

            speed = int(abs(dy) * 1200)

            if dy > 0.01:

                pyautogui.scroll(-speed)

            elif dy < -0.01:

                pyautogui.scroll(speed)

            self.prev_scroll_y = y

        else:

            self.prev_scroll_y = None