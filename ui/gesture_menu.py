import cv2


class GestureMenu:

    def __init__(self):

        self.items = ["Terminal", "Browser", "Files"]

        self.visible = False

        self.selected = -1

    def toggle(self):

        self.visible = not self.visible

    def draw(self, frame):

        if not self.visible:
            return frame

        h, w, _ = frame.shape

        start_y = 150

        for i, item in enumerate(self.items):

            x = int(w/2 - 120)
            y = start_y + i*80

            color = (80,80,80)

            if i == self.selected:
                color = (0,255,0)

            cv2.rectangle(
                frame,
                (x,y),
                (x+240,y+60),
                color,
                -1
            )

            cv2.putText(
                frame,
                item,
                (x+30,y+40),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0,0,0),
                2
            )

        return frame

    def update_selection(self, landmarks):

        if not self.visible:
            return None

        y = landmarks[8][1]

        if y < 0.4:
            self.selected = 0

        elif y < 0.6:
            self.selected = 1

        else:
            self.selected = 2

        return self.selected