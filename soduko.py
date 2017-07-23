import cv2
import numpy as np

img = cv2.imread('/home/lin/001.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret , thresh = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
kernel = np.uint8(np.zeros((3,3)))
for i in range(3):
    kernel[i][1] = 1
    kernel[1][i] = 1

eroded = cv2.erode(thresh,kernel)
cv2.imshow('eroded',eroded)
image , contours , hierarchy = cv2.findContours(eroded,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
number_boxes = []
number_contour = []
rectangles = []
print hierarchy[0]
for h in range(len(hierarchy[0])):
    if hierarchy[0][h][3] == 0:
        number_boxes.append(hierarchy[0][h])
print number_boxes
for k in range(len(number_boxes)):
    if number_boxes[k][2] != -1:
        number_contour.append(contours[number_boxes[k][2]])
print number_contour
for j in range(len(number_contour)):
    x,y,w,h = cv2.boundingRect(number_contour[j])
    rectangles.append([x,y,w,h])
    cv2.rectangle(img,(x,y),(x + w,y + h),(0,0,255),2)
cv2.imshow('img',img)
cv2.waitKey(0)



