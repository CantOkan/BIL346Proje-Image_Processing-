import numpy as np
from collections import deque
import cv2
from pynput.keyboard import Key,Controller
import imutils
import pyautogui

def StartObj():
    #105
    lower_bound=np.array([105,50,50])
    #135
    upper_bound=np.array([135,255,255])

    Points=deque(maxlen=100)


    cap=cv2.VideoCapture(0)
    turn=0
    direction=""
    last_pressed = ''

    keyboard=Controller()

    while(True):
        ret,frame=cap.read()
        frame=cv2.flip(frame,1)
        frame=imutils.resize(frame,width=600,height=600)
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        mask=cv2.inRange(hsv, lower_bound, upper_bound)

        kernel=np.ones((5,5),np.int8)


        opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)

        dilated=cv2.dilate(opening,kernel,iterations=1)

        res=cv2.bitwise_and(frame,frame,mask=dilated)


        e,contours,s=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)


        if(len(contours))>0:
            cv2.drawContours(res, contours, -1, (255,0,0), 3)
            c=max(contours,key=cv2.contourArea)#max Counter'ı bul
            ((x,y),radius)=cv2.minEnclosingCircle(c)

            center= (int(x),int(y))
            radius=int(radius)
            #cv2.circle(frame,center,radius,(0,255,0),2)

            M=cv2.moments(c) #kütlenin merkezini bulmamızı sağlar
            if(M["m00"] != 0 and M["m10"]!=0):
                cx=int(M["m10"]/M["m00"])
                cy=int(M['m01']/M["m00"])
                center_of_Mass=(cx,cy)

            if(radius>5):#radius<50
                print("Radius:{}".format(radius))
                cv2.circle(frame, center,radius, color=(255,0,0), thickness=-1)
                cv2.circle(frame, center_of_Mass, 10, color=(0,0,255), thickness=-1)#Center of MASS
                Points.append(center_of_Mass)

            for i in range(1, len(Points)):
                #If no points detected,move on
                if(Points[i-1]==None or Points[i] == None):
                    continue

                if(len(Points)>10):
                    if(turn>=10 and i==1 and Points[-10]!=None):
                        dx=Points[i-10][0]-Points[i][0]
                        dy=Points[i-10][1]-Points[i][1]
                        print("dx:{} dy:{}".format(dx,dy))
                        (dirX,dirY)=('','')


                        if np.abs(dx)>80:
                            if(np.sign(dx)==1):
                                dirX='Right'

                            else:
                                dirX='Left'

                        if np.abs(dy)>80:
                            if(int(dy)>0):
                                dirY='DOWN'
                            else:
                                dirY='UP'

                        if(dirX != ''):
                            direction=dirX
                        else:
                            direction=dirY


                        cv2.putText(frame, direction, (300,300), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 3)



        if(direction=='Right'):
            if(last_pressed !='right'):
                print("right \n")
                keyboard.press("d")
                keyboard.release("d")
                last_pressed='right'

        elif(direction=="DOWN"):
            if(last_pressed!='down'):
                print("down \n")
                keyboard.press("s")
                keyboard.release("s")
                last_pressed="down"


        elif(direction=='Left'):
            if(last_pressed!='left'):
                print("left \n")
                keyboard.press("a")
                keyboard.release("a")
                last_pressed="left"

        elif(direction!="UP"):
            if(last_pressed!='up'):
                print("up \n")
                keyboard.press("w")
                keyboard.release("w")
                last_pressed="up"



        cv2.imshow("Frame", frame)
        cv2.imshow("res", res)
        key=cv2.waitKey(1)
        if(key==120):# ascii code X=120
            break

        turn+=1

    cap.release()
    cv2.destroyAllWindows()


StartObj()
