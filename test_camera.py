import cv2
import numpy as np


cap=cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)


if cap.isOpened():
    ret, a=cap.read()



    while ret:
        ret,a=cap.read()
        cv2.imshow("camera",a)

        if cv2.waitKey(1) & 0xFF ==27:
            break

cap.release()
cv2.destroyAllWindows()