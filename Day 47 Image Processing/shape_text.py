import cv2
import numpy as np

img = np.zeros((512, 512, 3))

# rectangle
cv2.rectangle(img, pt1=(100, 100), pt2=(300, 300), color=(255, 0, 0), thickness=-1)
# circle
cv2.circle(img, center=(100, 400), radius=50, color=(0,0,255), thickness=-1)
# line
cv2.line(img, pt1=(0,0), pt2=(512,512),color=(0,255,0), thickness=2)
# text
cv2.putText(img,text="Hello", org=(100, 100), fontScale=4, color=(0,255,255), thickness=2, lineType=cv2.LINE_AA, fontFace=cv2.FONT_ITALIC) 

cv2.imshow("img", img)
cv2.waitKey(0)