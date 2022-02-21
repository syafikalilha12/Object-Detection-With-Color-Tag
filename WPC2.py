import cv2
import numpy as np
from numpy.lib.function_base import _parse_input_dimensions

def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)
def nothing(x):

    pass
img=cv2.imread('test.png')
cv2.namedWindow("TB Hijau")
cv2.resizeWindow("TB Hijau",640,240)
cv2.createTrackbar("L-H","TB Hijau",0,180,nothing)
cv2.createTrackbar("L-S","TB Hijau",0,255,nothing)
cv2.createTrackbar("L-V","TB Hijau",0,255,nothing)
cv2.createTrackbar("U-H","TB Hijau",180,180,nothing)
cv2.createTrackbar("U-S","TB Hijau",255,255,nothing)
cv2.createTrackbar("U-V","TB Hijau",255,255,nothing)
cv2.createTrackbar("AreaHijau","TB Hijau",300,3000,nothing)
cv2.namedWindow("TB Merah")
cv2.resizeWindow("TB Merah",640,240)
cv2.createTrackbar("L-H","TB Merah",0,180,nothing)
cv2.createTrackbar("L-S","TB Merah",0,255,nothing)
cv2.createTrackbar("L-V","TB Merah",0,255,nothing)
cv2.createTrackbar("U-H","TB Merah",180,180,nothing)
cv2.createTrackbar("U-S","TB Merah",255,255,nothing)
cv2.createTrackbar("U-V","TB Merah",255,255,nothing)
cv2.createTrackbar("AreaMerah","TB Merah",300,3000,nothing)
cv2.namedWindow("TB Biru")
cv2.resizeWindow("TB Biru",640,240)
cv2.createTrackbar("L-H","TB Biru",0,180,nothing)
cv2.createTrackbar("L-S","TB Biru",0,255,nothing)
cv2.createTrackbar("L-V","TB Biru",0,255,nothing)
cv2.createTrackbar("U-H","TB Biru",180,180,nothing)
cv2.createTrackbar("U-S","TB Biru",255,255,nothing)
cv2.createTrackbar("U-V","TB Biru",255,255,nothing)
cv2.createTrackbar("AreaBiru","TB Biru",300,3000,nothing)    
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
        area= cv2.contourArea(cnt)
        nilaiarea = cv2.getTrackbarPos("AreaHijau","TB Hijau")
        if area > nilaiarea:
            M = cv2.moments(cnt)
            try:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                pus = (cx,cy)
            except:
                pass
            (x,y),radius=cv2.minEnclosingCircle(cnt)
            center=(int(x),int(y))
            resultImg=cv2.circle(resultImg,center,int(radius),(255,0,0),3)
            cv2.putText(resultImg,"Hijau",(center),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            cv2.putText(resultImg,"("+str(pus[0])+","+str(pus[1])+")", (pus[0]+10,pus[1]+15), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255, 0, 0),1)

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
        area= cv2.contourArea(cnt)
        nilaiarea = cv2.getTrackbarPos("AreaMerah","TB Merah")
        if area > nilaiarea:
            M = cv2.moments(cnt)
            try:
                cx1 = int(M['m10']/M['m00'])
                cy1 = int(M['m01']/M['m00'])
                pus1 = (cx1,cy1)
            except:
                pass
            (x,y),radius=cv2.minEnclosingCircle(cnt)
            center=(int(x),int(y))
            resultImg1=cv2.circle(resultImg1,center,int(radius),(255,0,0),3)
            cv2.putText(resultImg1,"Merah",(center),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            cv2.putText(resultImg1,"("+str(pus1[0])+","+str(pus1[1])+")", (pus1[0]+10,pus1[1]+15), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255, 0, 0),1)
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
        area= cv2.contourArea(cnt)
        nilaiarea = cv2.getTrackbarPos("AreaBiru","TB Biru")
        if area > nilaiarea:
            M = cv2.moments(cnt)
            try:
                cx2 = int(M['m10']/M['m00'])
                cy2 = int(M['m01']/M['m00'])
                pus2 = (cx2,cy2)
            except:
                pass
            (x,y),radius=cv2.minEnclosingCircle(cnt)
            center=(int(x),int(y))
            resultImg2=cv2.circle(resultImg2,center,int(radius),(255,0,0),3)
            cv2.putText(resultImg2,"Biru",(center),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))
            cv2.putText(resultImg2,"("+str(pus2[0])+","+str(pus2[1])+")", (pus2[0]+10,pus2[1]+15), cv2.FONT_HERSHEY_COMPLEX, 0.4,(255, 0, 0),1)

    if cy<cy1 and cx<cx1:
        if cx2>cx and cy2<cy1:
            print("Kursi")
            cv2.putText(resultImg2,"Kursi",(0,10), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1)
    if cy1==cy2 and cx1<cx:
        if cx2==cx and cy<cy2:
            print("Papan")
            cv2.putText(resultImg2,"Papan",(0,10), cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1)
    if cy2<cy and cx2<cx1:
        if cy>cy1 and cx==cx1:
            print("Monitor")
            cv2.putText(resultImg2,"Monitor",(0,10),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1)
    if cy1<cy2 and cx1==cx2:
        if cy==cy1 and cx>cx1:
            print("Laptop")
            cv2.putText(resultImg2,"Laptop",(0,10),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1)
    if cx==cx1 and cy<cy2:
        if cx2==cx and cy2<cy1:
            if cx1==cx and cy1>cy2:
                print("Keyboard")
                cv2.putText(resultImg2,"Keyboard",(0,10),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1)
    if cx2==cx1 and cy2<cy1:
        if cx1==cx2 and cy1<cy:
            if cx==cx1 and cy>cy1:
                print("Meja")
                cv2.putText(resultImg2,"Meja",(0,10),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1)
    if cx1==cx and cy1<cy:
        if cx==cx1 and cy<cy2:
            if cx2==cx and cy2>cy:
                print("PC")
                cv2.putText(resultImg2,"PC",(0,10),cv2.FONT_HERSHEY_COMPLEX, 0.5,(255, 0, 0),1) 
    cv2.imshow('Hasil',resultImg2)
    key=cv2.waitKey(1)
    if key==27:
        break

cv2.destroyAllWindows()