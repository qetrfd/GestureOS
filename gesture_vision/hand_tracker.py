import cv2
import mediapipe as mp
import math


class HandTracker:

    def __init__(self):

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            model_complexity=0,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6
        )

        self.mp_draw = mp.solutions.drawing_utils

    def valid_hand(self, landmarks):

        wrist = landmarks[0]
        index = landmarks[8]

        dx = wrist[0] - index[0]
        dy = wrist[1] - index[1]

        dist = math.sqrt(dx*dx + dy*dy)

        return dist > 0.08

    def detect(self, frame):

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        result = self.hands.process(rgb)

        hands = []

        if result.multi_hand_landmarks:

            for hand_landmarks in result.multi_hand_landmarks:

                landmarks = []

                for lm in hand_landmarks.landmark:
                    landmarks.append((lm.x, lm.y, lm.z))

                if self.valid_hand(landmarks):

                    hands.append(landmarks)

                    self.mp_draw.draw_landmarks(
                        frame,
                        hand_landmarks,
                        self.mp_hands.HAND_CONNECTIONS
                    )

        return frame, hands