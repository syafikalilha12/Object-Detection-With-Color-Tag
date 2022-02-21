import cv2
import numpy as np

def nothing(x):

    pass

img=cv2.imread('test1.png')
cv2.namedWindow("TB")
cv2.createTrackbar("L-H","TB",0,180,nothing)
cv2.createTrackbar("L-S","TB",0,255,nothing)
cv2.createTrackbar("L-V","TB",0,255,nothing)
cv2.createTrackbar("U-H","TB",180,180,nothing)
cv2.createTrackbar("U-S","TB",255,255,nothing)
cv2.createTrackbar("U-V","TB",255,255,nothing)

while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("L-H","TB")
    l_s=cv2.getTrackbarPos("L-S","TB")
    l_v=cv2.getTrackbarPos("L-V","TB")
    u_h=cv2.getTrackbarPos("U-H","TB")
    u_s=cv2.getTrackbarPos("U-S","TB")
    u_v=cv2.getTrackbarPos("U-V","TB")
    lower=np.array([l_h,l_s,l_v])
    upper=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower,upper)
    cv2.imshow("Mask",mask)
    cv2.imshow("norml",img)
    key=cv2.waitKey(1)
    if key==27:
        break
        
cam.release()
cv2.destroyAllWindows()