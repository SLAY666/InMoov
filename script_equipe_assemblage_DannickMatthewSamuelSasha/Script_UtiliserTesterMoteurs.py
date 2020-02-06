import time
from adafruit_servokit import ServoKit

inMoov = ServoKit(channels=16)
inMoov.servo[3].actuation_range = 180
inMoov.servo[3].set_pulse_width_range(556,2420)

angDepart = int(input("angle"))
inMoov.servo[3].angle = angDepart

print("connectez le servo au port 3 du module\n")

#while True:
	#angle = int(input("angle: "))

while True:
	ang = float(input("angle"))
	inMoov.servo[3].angle = ang
