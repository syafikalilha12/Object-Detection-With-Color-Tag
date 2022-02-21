import cv2
import numpy as np
def empty(a):
    pass
cv2.namedWindow('Tuning Parameters')
cv2.resizeWindow('Tuning Parameters',640,240)
cv2.createTrackbar("threshold1","Tuning Parameters",150,300, empty)
cv2.createTrackbar("threshold2","Tuning Parameters",255,300, empty)
img = cv2.imread('test.png', cv2.IMREAD_GRAYSCALE)
while True:
    imgcontour=img.copy()
    threshold1 = cv2.getTrackbarPos("threshold1","Tuning Parameters")
    threshold2 = cv2.getTrackbarPos("threshold2","Tuning Parameters")
    _, threshold= cv2.threshold(img,threshold1,threshold2, cv2.THRESH_BINARY)
    _, contours= cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(imgcontour, cnt, -1, (255,0,255), 7)
    cv2.imshow('bentuk',img)
    cv2.imshow('threshold', threshold)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
img.release()
cv2.destroyAllWindows()