import cv2
import time

from gesture_vision.camera import Camera
from gesture_vision.hand_tracker import HandTracker

from utils.fps_counter import FPSCounter
from utils.landmark_filter import LandmarkFilter
from utils.gesture_detector import is_activation_sign

from utils.two_hand_zoom import TwoHandZoom
from utils.rotation_gesture import RotationGesture

from control.mouse_control import MouseControl

from ui.cursor_overlay import CursorOverlay
from ui.palm_overlay import PalmOverlay


def main():

    camera = Camera(width=640, height=480)
    tracker = HandTracker()
    filter = LandmarkFilter()

    mouse = MouseControl()
    zoom = TwoHandZoom()
    rotation = RotationGesture()

    cursor = CursorOverlay(640, 480)
    palm = PalmOverlay(640, 480)

    fps = FPSCounter()

    gesture_mode = False

    # temporizadores SOLO para activación
    activation_start = None
    activation_delay = 1.5
    activation_locked = False


    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        frame, hands = tracker.detect(frame)

        filtered_hands = []

        if hands:
            for hand in hands:
                filtered_hands.append(filter.apply(hand))

        if len(filtered_hands) == 1:

            hand = filtered_hands[0]

            # ---- GESTO DE ACTIVACIÓN (requiere mantener 1.5 s) ----
            if is_activation_sign(hand):

                if activation_start is None:
                    activation_start = time.time()

                elif time.time() - activation_start >= activation_delay and not activation_locked:

                    gesture_mode = not gesture_mode
                    activation_locked = True

            else:

                activation_start = None
                activation_locked = False

            # ---- CONTROLES NORMALES SIN DELAY ----
            if gesture_mode:

                mouse.move(hand)
                mouse.click(hand)
                mouse.drag(hand)
                mouse.scroll(hand)

            # rotación
            rot = rotation.update(hand)

            if rot == "ROTATE_RIGHT":

                cv2.putText(
                    frame,
                    "ROTATE RIGHT",
                    (380, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 255),
                    3
                )

            if rot == "ROTATE_LEFT":

                cv2.putText(
                    frame,
                    "ROTATE LEFT",
                    (380, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 255),
                    3
                )

        elif len(filtered_hands) == 2:

            zoom.update(filtered_hands)

        # ---- CURSOR OVERLAY ----
        landmark_hand = filtered_hands[0] if filtered_hands else None

        frame = cursor.draw(
            frame,
            landmark_hand,
            mouse.dragging,
            mouse.prev_scroll_y is not None
        )

        # ---- PALM OVERLAY ----
        if landmark_hand:

            fist_detected = mouse.is_fist(landmark_hand)
            frame = palm.draw(frame, landmark_hand, fist_detected)

        fps.update()
        frame = fps.draw(frame)

        mode_text = "GESTURE MODE ON" if gesture_mode else "GESTURE MODE OFF"

        cv2.putText(
            frame,
            mode_text,
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("GestureOS", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()