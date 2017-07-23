#!/usr/bin/python
import cv2

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
while(True):
     ret, cap_img = cap.read()
     ret2, cap_img2 = cap2.read()
     gray = cv2.cvtColor(cap_img,cv2.COLOR_BGR2GRAY)
     th = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
     cv2.imshow('frame2',cap_img2)
     cv2.imshow('frame',gray)
     if cv2.waitKey(1) & 0xFF == ord('q'):
         break
cap.release()
cv2.destroyAllWindows()


