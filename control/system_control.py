import pyautogui
import time


class SystemControl:

    def __init__(self):

        self.last_action = 0
        self.cooldown = 1.0

    def can_execute(self):

        now = time.time()

        if now - self.last_action > self.cooldown:
            self.last_action = now
            return True

        return False

    def execute(self, gesture):

        if not self.can_execute():
            return

        if gesture == 0:
            pyautogui.press("volumeup")

        elif gesture == 1:
            pyautogui.press("volumedown")

        elif gesture == 2:
            pyautogui.press("volumemute")

        elif gesture == 3:
            pyautogui.hotkey("command", "shift", "4")

        elif gesture == 4:
            pyautogui.click()

        elif gesture == 5:
            pyautogui.press("space")