
import cv2
import numpy as np
img = cv2.imread('/home/lin/001.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret ,thresh = cv2.threshold(gray,170,255,1)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(20,20))
dilated = cv2.dilate(thresh,kernel)
cv2.imshow('dilated',dilated)
image, contours , hierarchy = cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

boxes = []
for i in range(len(hierarchy[0])):
    if hierarchy[0][i][3] == 0:
        boxes.append(hierarchy[0][i])

number_boxes = []
numbers = []
samples = []
labels = []
for j in range(len(boxes)):
    if boxes[j][2] != -1:
        x,y,w,h = cv2.boundingRect(contours[boxes[j][2]])
        number_boxes.append([x,y,w,h])
        img = cv2.rectangle(img,(x-1,y-1),(x+w+1,y+h+1),(0,0,255),2)

numberBox_sorted = sorted(number_boxes,key = lambda t : t[0])

for i in range(len(numberBox_sorted)):
    [x1,y1,w1,h1] = numberBox_sorted[i]
    number_img - thresh[x1-1:x1+w1+1,y1-1:y1-h1+1]
    numbers.append(number_img)



for i,number in numbers:
    number_resized = cv2.resize(number,(20,40))
    number_save = number_resized.reshape((1,800))
    number_save = number_save/255.
    samples.append(number_save)
    labels.append(float(i))
np.arr


img_resized = cv2.resize(img,(400,400))
cv2.imshow("img",img_resized)
cv2.waitKey(0)


