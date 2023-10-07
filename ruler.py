# Measure Pixel Distances

import HandTrackingModule as htm
import cv2
import math

cap = cv2.VideoCapture(1)
detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)

    try:   
        lmList1 = detector.findPosition(img, handNo=0)
        lmList2 = detector.findPosition(img, handNo=1)

        x1, y1 = lmList1[9][1], lmList1[9][2]
        x2, y2 = lmList2[9][1], lmList2[9][2]

        length = math.hypot(x2 - x1, y2 - y1)
        
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.putText(img, str(int(length)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2) 
    except IndexError:
        pass   

    cv2.imshow("Image", img)
    cv2.waitKey(1)
