import random
import time
from playsound import playsound

data = []
becker = []
# freq is set at 50

for i in range(8):
	rand = random.randint(0,1)
	data.append(rand)

for i in data:
	penis = random.randint(2,16)
	rhy = float(penis) / 40
	print(i)
	if i == 1:
		print(rhy)
		becker.append(rhy)
		playsound('audio.mp3')
		time.sleep(rhy)
	elif i == 0:
		print(rhy)
		becker.append(rhy)
		time.sleep(rhy)

for i in becker:
	print(i)

