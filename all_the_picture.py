# encodeing UTF-8
import cv2
import glob as gb

img_path = gb.glob("/home/lin/numbers/*")

for path in img_path:
    print path
    img = cv2.imread(path)
    cv2.imshow("picture",img)
    cv2.waitKey(1000)

