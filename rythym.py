import time
from random import random

from playsound import playsound
# f = open("/Users/erandoni/rythmformat", "r")
# filelength = int(f.readline())

for i in range(20):
    temp = random()
    if temp < 0.33333:
        playsound('/Users/erandoni/Downloads/piano-g-6200.mp3')
    elif 0.333333333 < temp < 0.66666666:
        playsound('/Users/erandoni/Downloads/punch-boxing-02wav-14897.mp3')
    else:
        playsound('/Users/erandoni/Downloads/bicycle-horn-7126.mp3')
    time.sleep(random())
