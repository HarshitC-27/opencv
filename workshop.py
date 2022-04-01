import cv2
import math
import mediapipe as mp
import time
import keyboard         #pip install keyboard

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands                                          
hands = mpHands.Hands(max_num_hands = 1)
mpDraw = mp.solutions.drawing_utils
pTime = 0
dia = 30
radi = int(dia/2)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmark.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w), int(lm.y*h)
                # 1 tip
                if id==8:       
                    cv2.circle(img,(cx,cy),radi,(255,0,255),cv2.FILLED)
                    f1 = (cx,cy)
                # 2 tip
                elif id==12:       
                    cv2.circle(img,(cx,cy),radi,(255,0,255),cv2.FILLED)
                    f2 = (cx,cy)
                # 3 tip
                elif id==16:       
                    cv2.circle(img,(cx,cy),radi,(255,0,255),cv2.FILLED)
                    f3 = (cx,cy)
                # 4 tip
                elif id==20:       
                    cv2.circle(img,(cx,cy),radi,(255,0,255),cv2.FILLED)
                    f4 = (cx,cy)
                # thumb tip
                elif id==4:       
                    cv2.circle(img,(cx,cy),radi,(255,0,255),cv2.FILLED)
                    ft = (cx,cy)
                #index base
                elif id==5:
                    cv2.circle(img,(cx,cy),radi,(255,0,255),cv2.FILLED)
                    bt = (cx,cy)
            t = 50
            if(math.sqrt(((f2[0]-ft[0])**2)+((f2[1]-ft[1])**2) )<=dia):
                while t:
                    keyboard.press_and_release('w')
                    t=t-1
            elif(math.sqrt(((f1[0]-ft[0])**2)+((f1[1]-ft[1])**2) )<=dia):
                while t:
                    keyboard.press_and_release('a')
                    t=t-1
            elif(math.sqrt(((f3[0]-ft[0])**2)+((f3[1]-ft[1])**2) )<=dia):
                while t:
                    keyboard.press_and_release('d')
                    t=t-1
            elif(math.sqrt(((f4[0]-ft[0])**2)+((f4[1]-ft[1])**2) )<=dia):
                while t:
                    keyboard.press_and_release('s')
                    t=t-1
            elif(math.sqrt(((bt[0]-ft[0])**2)+((bt[1]-ft[1])**2) )<=dia):
                while t:
                    keyboard.press_and_release(' ')
                    t=t-1
            
                
            mpDraw.draw_landmarks(img, hand_landmark, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime 

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,
                3,(255,0,255),3)

    cv2.imshow("Image", img)
    cv2.waitKey(1),                      