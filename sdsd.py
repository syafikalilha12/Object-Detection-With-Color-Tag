import cv2
import numpy as np

def nothing(x):
    pass

img=cv2.imread('test1.png')
cv2.namedWindow("TB Hijau")
cv2.createTrackbar("L-H","TB Hijau",0,180,nothing)
cv2.createTrackbar("L-S","TB Hijau",0,255,nothing)
cv2.createTrackbar("L-V","TB Hijau",0,255,nothing)
cv2.createTrackbar("U-H","TB Hijau",180,180,nothing)
cv2.createTrackbar("U-S","TB Hijau",255,255,nothing)
cv2.createTrackbar("U-V","TB Hijau",255,255,nothing)
cv2.namedWindow("TB Merah")
cv2.createTrackbar("L-H","TB Merah",0,180,nothing)
cv2.createTrackbar("L-S","TB Merah",0,255,nothing)
cv2.createTrackbar("L-V","TB Merah",0,255,nothing)
cv2.createTrackbar("U-H","TB Merah",180,180,nothing)
cv2.createTrackbar("U-S","TB Merah",255,255,nothing)
cv2.createTrackbar("U-V","TB Merah",255,255,nothing)
cv2.namedWindow("TB Biru")
cv2.createTrackbar("L-H","TB Biru",0,180,nothing)
cv2.createTrackbar("L-S","TB Biru",0,255,nothing)
cv2.createTrackbar("L-V","TB Biru",0,255,nothing)
cv2.createTrackbar("U-H","TB Biru",180,180,nothing)
cv2.createTrackbar("U-S","TB Biru",255,255,nothing)
cv2.createTrackbar("U-V","TB Biru",255,255,nothing)    
while True:
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_hH=cv2.getTrackbarPos("L-H","TB Hijau")
    l_sH=cv2.getTrackbarPos("L-S","TB Hijau")
    l_vH=cv2.getTrackbarPos("L-V","TB Hijau")
    u_hH=cv2.getTrackbarPos("U-H","TB Hijau")
    u_sH=cv2.getTrackbarPos("U-S","TB Hijau")
    u_vH=cv2.getTrackbarPos("U-V","TB Hijau")
    lowerHijau=np.array([l_hH,l_sH,l_vH])
    upperHijau=np.array([u_hH,u_sH,u_vH])
    maskhijau=cv2.inRange(hsv,lowerHijau,upperHijau)
    cv2.imshow("Mask Hijau",maskhijau)
    kernal = np.ones((25,25),"uint8")
    contours= cv2.findContours(maskhijau, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    resultImg=(img).copy()
    contour=[]
    for i in range(len(contours)):
        cnt=contours[i]
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        center=(int(x),int(y))
        resultImg=cv2.circle(resultImg,center,int(radius),(255,0,0),3)
        cv2.putText(resultImg,"Hijau",(center),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
    ##Warna Merah
    l_hM=cv2.getTrackbarPos("L-H","TB Merah")
    l_sM=cv2.getTrackbarPos("L-S","TB Merah")
    l_vM=cv2.getTrackbarPos("L-V","TB Merah")
    u_hM=cv2.getTrackbarPos("U-H","TB Merah")
    u_sM=cv2.getTrackbarPos("U-S","TB Merah")
    u_vM=cv2.getTrackbarPos("U-V","TB Merah")
    lowerMerah=np.array([l_hM,l_sM,l_vM])
    upperMerah=np.array([u_hM,u_sM,u_vM])
    maskMerah=cv2.inRange(hsv,lowerMerah,upperMerah)
    cv2.imshow("Mask Merah",maskMerah)
    contours= cv2.findContours(maskMerah, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    resultImg1=(resultImg).copy()
    contour=[]
    for i in range(len(contours)):
        cnt=contours[i]
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        center=(int(x),int(y))
        resultImg1=cv2.circle(resultImg1,center,int(radius),(255,0,0),3)
        cv2.putText(resultImg1,"Merah",(center),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
    #cv2.imshow("image full",resultImg1)
    l_hB=cv2.getTrackbarPos("L-H","TB Biru")
    l_sB=cv2.getTrackbarPos("L-S","TB Biru")
    l_vB=cv2.getTrackbarPos("L-V","TB Biru")
    u_hB=cv2.getTrackbarPos("U-H","TB Biru")
    u_sB=cv2.getTrackbarPos("U-S","TB Biru")
    u_vB=cv2.getTrackbarPos("U-V","TB Biru")
    lowerBiru=np.array([l_hB,l_sB,l_vB])
    upperBiru=np.array([u_hB,u_sB,u_vB])
    maskBiru=cv2.inRange(hsv,lowerBiru,upperBiru)
    cv2.imshow("Mask Biru",maskBiru)
    contours= cv2.findContours(maskBiru, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    resultImg2=(resultImg1).copy()
    contour=[]
    for i in range(len(contours)):
        cnt=contours[i]
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        center=(int(x),int(y))
        resultImg2=cv2.circle(resultImg2,center,int(radius),(255,0,0),3)
        cv2.putText(resultImg2,"Biru",(center),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
    cv2.imshow('Hasil',resultImg2)
    key=cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()