import HandTrackingModule as htm
import cv2
import math
import random
import time
from playsound import playsound
from datetime import datetime

cap = cv2.VideoCapture(1)
detector = htm.handDetector(0.25)

prevTime = 0
currTime = 0

data = []
becker = []
timers = []


for i in range(8):
    rand = random.randint(0, 1)
    data.append(rand)

detector = htm.handDetector()

claps = 0
handstogether = False

for i in data:
    temp = random.randint(2, 16)
    rhy = float(temp) / 40
    print(i)
    if i == 1:
        print(rhy)
        becker.append(rhy)
        playsound('audio.mp3')
        time.sleep(rhy)
    elif i == 0:
        print(rhy)
        becker.append(rhy)
        playsound('audio.mp3')
        time.sleep(rhy)

tempo = [0.0] * 9
run = True

while run:
    clapped = False
    beeped = False
    start = 0
    (success, img) = cap.read()
    img = detector.findHands(img)
    length = 0
    try:
        lmList1 = detector.findPosition(img, handNo=0)
        lmList2 = detector.findPosition(img, handNo=1)

        (x1, y1) = (lmList1[9][1], lmList1[9][2])
        (x2, y2) = (lmList2[9][1], lmList2[9][2])

        length = math.hypot(x2 - x1, y2 - y1)

        if not handstogether and length < 60:  # a clap was seen
            tempo[claps] = datetime.now()
            claps += 1
            if claps == 1:
                time.sleep(3)
            handstogether = True
        elif handstogether and length > 110:

                                            # a clap was not seen

            handstogether = False

    except IndexError:

        if handstogether == False and claps > 0:
            tempo[claps] = datetime.now()
            claps += 1
            if claps == 1:
                time.sleep(3)
            handstogether = True
    cv2.putText(
        img,
        str(int(claps)),
        (10, 70),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (0, 0, 255),
        2,
        )
    cv2.putText(
        img,
        str(int(length)),
        (10, 120),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255, 0, 0),
        2,
        )

    '''cv2.putText(
        img,
        str(timers),
        (10, 170),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255, 255, 0),
        2,
        )'''

    # cv2.putText(
    #     img,
    #     str(becker),
    #     (10, 220),
    #     cv2.FONT_HERSHEY_PLAIN,
    #     3,
    #     (255, 0, 0),
    #     2,
    #     )
    cv2.imshow('Image', img)
    cv2.waitKey(1)
    end = time.time()
    if claps >= 9:
        run = False


time_diffs = [(tempo[i] - tempo[i-1]).total_seconds() for i in range (1, len(tempo))]
totaldiff = 0


for i in range (len(becker)):
    totaldiff += becker[i]
for i in range (len(time_diffs)):
        totaldiff -= time_diffs[i]

totaldiff = abs(totaldiff) - 5
score = 10000 - (1000 * totaldiff)
if score < 0:
    score = 0

img = cv2.imread('elgato.jpg', cv2.IMREAD_ANYCOLOR)

cv2.putText(
        img,
        'you were off by a total of ' + str(round(totaldiff,2)),
        (40, 1000),
        cv2.FONT_HERSHEY_PLAIN,
        6,
        (255, 0, 0),
        10,
        )
cv2.putText(
        img,
        'SCORE:   ' + str(score),
        (40, 500),
        cv2.FONT_HERSHEY_PLAIN,
        6,
        (0, 0, 255),
        10,
        )
cv2.imshow('Image', img)
cv2.waitKey(0)
