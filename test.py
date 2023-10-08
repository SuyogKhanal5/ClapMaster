import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BOARD)
GPIO.setup(1,GPIO.OUT)
servo = GPIO.PWM(1, 50)
data = []

for i in range(20):
	rand = random.randint(0, 1)
	data.append(rand)

for i in data:
	print(i)

servo.start(0)
print("waiting for one second")
time.sleep(1)

print("rotating at intervals of 12 degrees")
duty = 2
while duty <= 170:
	servo.ChangeDutyCycle(duty)
	time.sleep(1)
	duty = duty+1

print("turning back to 0")
servo.ChangeDutyCycle(2)
time.sleep(1)
servo.ChangeDutyCycle(0)


servo.stop()
GPIO.cleanup()
print("done!")
