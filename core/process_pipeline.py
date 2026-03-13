from multiprocessing import Process, Queue
import cv2

from gesture_vision.camera import Camera
from gesture_vision.hand_tracker import HandTracker


def camera_process(frame_queue, landmark_queue):

    camera = Camera(width=640, height=480)
    tracker = HandTracker()

    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        frame, landmarks = tracker.detect(frame)

        if not frame_queue.full():
            frame_queue.put(frame)

        if not landmark_queue.full():
            landmark_queue.put(landmarks)


def ui_process(landmark_queue):

    from ui.spatial_desktop import SpatialDesktop

    desktop = SpatialDesktop()

    while True:

        if not landmark_queue.empty():

            landmarks = landmark_queue.get()

            if len(landmarks) == 21:
                desktop.update(landmarks)

        desktop.render()