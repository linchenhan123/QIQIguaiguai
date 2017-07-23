import cv2
import glob as gb
import numpy as np

img_path = gb.glob("/home/lin/numbers/*")

k = 0
labels = []
samples =  []
for path in img_path:
    img  = cv2.imread(path)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    image, contours, hierarchy =    cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    height,width = img.shape[:2]
    w = width/5
    rect_list = []
    list1 = []
    list2 = []
    print path
    for cnt in contours:
        #if cv2.contourArea(cnt)>100:
        [x,y,w,h] = cv2.boundingRect(cnt)

        if w > 30 and  h  > (height/4):
            if y < (height/2):
                list1.append([x,y,w,h])
            else:
                list2.append([x,y,w,h])
    list1_sorted = sorted(list1,key = lambda t : t[0])
    list2_sorted = sorted(list2,key = lambda t : t[0])
    for i in range(5):
        [x1,y1,w1,h1] = list1_sorted[i]
        [x2,y2,w2,h2] = list2_sorted[i]
        number_roi1 = gray[y1:y1+h1, x1:x1+w1] #Cut the frame to size
        number_roi2 = gray[y2:y2+h2, x2:x2+w2] #Cut the frame to size
        resized_roi1=cv2.resize(number_roi1,(20,40))
        thresh1 = cv2.adaptiveThreshold(resized_roi1,255,1,1,11,2)

        resized_roi2=cv2.resize(number_roi2,(20,40))
        thresh2 = cv2.adaptiveThreshold(resized_roi2,255,1,1,11,2)
        number_path1 = "/home/lin/number/%s/%d" % (str(i),k) + '.jpg'
        j = i+5
        if j ==10:
            j = 0
        number_path2 = "/home/lin/number/%s/%d" % (str(j),k) + '.jpg'
        k+=1

        normalized_roi1 = thresh1/255.
        print thresh1
        #print "#######################"
        #print normalized_roi1
        normalized_roi2 = thresh2/255.
        cv2.imwrite(number_path1,thresh1)
        cv2.imwrite(number_path2,thresh2)

        sample1 = normalized_roi1.reshape((1,800))
        samples.append(sample1[0])
        labels.append(float(i))

        sample2 = normalized_roi2.reshape((1,800))
        samples.append(sample2[0])
        labels.append(float(j))
samples = np.array(samples,np.float32)
labels = np.array(labels,np.float32)
labels = labels.reshape((labels.size,1))
np.save('/home/lin/samples.npy',samples)
np.save('/home/lin/label.npy',labels)
print labels
