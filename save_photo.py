import numpy as np
import cv2

def go_snap(name_label):
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        [ok, frame] = cap.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('Photo', frame)

        key = cv2.waitKey(1)
        if key == ord('p'):
            cv2.imwrite(str("Images/")+str(name_label)+str(".jpg"), frame)
            break
    cv2.destroyAllWindows()
