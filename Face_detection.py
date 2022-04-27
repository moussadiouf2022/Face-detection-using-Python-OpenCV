import cv2 as cv
import numpy as np

im = cv.imread(r"C:\Users\hp\opencv_tuturial_python\image_5.jpg")
#cv.imshow('Image_1',im)

gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(im, (x,y),(x+w,y+h), (0,255,0), thickness=2)

cv.imshow ('Detected faces',im)
   
cv.waitKey(0)







