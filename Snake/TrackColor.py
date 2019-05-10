import cv2

import numpy as np

def nuthin(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars",0,180,nuthin)
cv2.createTrackbar("L-S", "Trackbars",0,255,nuthin)
cv2.createTrackbar("L-V", "Trackbars",0,255,nuthin)
cv2.createTrackbar("U-H", "Trackbars",0,179,nuthin)
cv2.createTrackbar("U-S", "Trackbars",0,255,nuthin)
cv2.createTrackbar("U-V", "Trackbars",0,255,nuthin)

#def getValues():


while True:
    ret,frame=cap.read()

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S", "Trackbars")
    l_v=cv2.getTrackbarPos("L-V", "Trackbars")

    u_h=cv2.getTrackbarPos("U-H", "Trackbars")
    u_s=cv2.getTrackbarPos("U-S", "Trackbars")
    u_v=cv2.getTrackbarPos("U-V", "Trackbars")

    lower_bound=np.array([l_h,l_s,l_v])

    upper_bound=np.array([u_h,u_s,u_v])

    #Create mask

    mask=cv2.inRange(hsv, lower_bound, upper_bound)

    final=cv2.bitwise_and(frame, frame, mask=mask)


    cv2.imshow('Hi',frame)
    cv2.imshow('mask', final)
    key=cv2.waitKey(1)
    if(key==120):# ascii code X=120
        break



cap.release()
cv2.destroyAllWindows()
