import cv2
import numpy as np

cap = cv2.imread('test1.png')

def empty(a):
    pass
cv2.namedWindow('Tuning Parameters')
cv2.resizeWindow('Tuning Parameters',640,240)
cv2.createTrackbar("threshold1","Tuning Parameters",150,300, empty)
cv2.createTrackbar("threshold2","Tuning Parameters",255,300, empty)
cv2.createTrackbar("area","Tuning Parameters",300,30000,empty)
def getContours(img,imgcontour):
    contours,hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        nilaiarea = cv2.getTrackbarPos("area","Tuning Parameters")
        if area > nilaiarea:
            #cv2.drawContours(imgcontour, cnt, -1, (255,0,255), 7)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 *peri, True)
            #print(len(approx))
            x,y,w,h = cv2.boundingRect(approx)
            cv2.rectangle(imgcontour, (x, y ), (x +w, y+h),(0,255,0),5)
            img1=((x, y ), (x +w, y+h))
            print(img1)
            cv2.putText(imgcontour, "points: "+str(len(approx)), (x+w+20, y+20), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2) 
            cv2.putText(imgcontour, "area: "+str(int(area)), (x+w+20, y+45), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            titik = len(approx)
            if titik == 4:
                cv2.putText(imgcontour,"Segi 4", (x+w+20, y+80),cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
while True:
    imgcontour = cap.copy()
    imgBlur = cv2.GaussianBlur(cap,(7, 7), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    threshold1 = cv2.getTrackbarPos("threshold1","Tuning Parameters")
    threshold2 = cv2.getTrackbarPos("threshold2","Tuning Parameters")
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)
    kernel = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)      
    getContours(imgDil,imgcontour)
    cv2.imshow("Hasil",imgcontour)
    cv2.imshow("dil",imgDil)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()