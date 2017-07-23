import cv2
import numpy as np

camera = cv2.VideoCapture(0)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    grabbed , frame = camera.read()
    fgmask = fgbg.apply(frame)

    eroded = cv2.erode(fgmask,kernel)
    cv2.imshow('fgmask',fgmask)
    cv2.imshow('frame',eroded)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
