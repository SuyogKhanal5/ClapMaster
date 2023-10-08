import HandTrackingModule as htm
import cv2
import math
import time

# change input if necessary for pi
cap = cv2.VideoCapture(1)
cap.set(cv2.cv.CV_CAP_PROP_FPS, 15)

detector = htm.handDetector(0.25)

prevTime = 0
currTime = 0

claps = 0

handsTogether = False

# Change the loop to something that makes more sense later

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    length = 0

    try:   
        lmList1 = detector.findPosition(img, handNo=0)
        lmList2 = detector.findPosition(img, handNo=1)

        x1, y1 = lmList1[9][1], lmList1[9][2]
        x2, y2 = lmList2[9][1], lmList2[9][2]

        length = math.hypot(x2 - x1, y2 - y1)

        if not handstogether and length < 75:
            claps += 1
            handstogether = True
        elif handstogether and length > 90:
            handstogether = False

    except IndexError:
        if handstogether == False and claps > 0: 
            claps += 1
            handstogether = True

    cv2.putText(img, str(int(claps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2) 
    cv2.putText(img, str(int(length)), (10,120), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 2) 

    cv2.imshow("Image", img) 
    cv2.waitKey(1) 