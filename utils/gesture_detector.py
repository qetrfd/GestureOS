def is_activation_sign(landmarks):

    thumb_tip = landmarks[4]
    thumb_joint = landmarks[3]

    pinky_tip = landmarks[20]
    pinky_joint = landmarks[18]

    index_tip = landmarks[8]
    index_joint = landmarks[6]

    middle_tip = landmarks[12]
    middle_joint = landmarks[10]

    ring_tip = landmarks[16]
    ring_joint = landmarks[14]


    thumb_out = abs(thumb_tip[0] - thumb_joint[0]) > 0.05

    pinky_up = pinky_tip[1] < pinky_joint[1]

    index_down = index_tip[1] > index_joint[1]
    middle_down = middle_tip[1] > middle_joint[1]
    ring_down = ring_tip[1] > ring_joint[1]


    return thumb_out and pinky_up and index_down and middle_down and ring_down