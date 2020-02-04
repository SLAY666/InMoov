from __future__ import print_function
import os
import rospy
from std_msgs.msg import String
import sys
import select
import tty
import termios
import xbox

joy=xbox.Joystick()

orig_settings =  termios.tcgetattr(sys.stdin)
# Format floating point number to string format -x.xxx
def fmtFloat(n):
    return '{:6.3f}'.format(n)

def talker():
	x = 0
	pub = rospy.Publisher('Buttons', String, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(2)
	button = "A"
	angle =  "90"
	i = 0
	while not rospy.is_shutdown():
		if joy.A()==1:
			button = "A"
			angle = str((1+joy.leftY())*45)
		if joy.X()==1:
			button = "X"
			angle = str((1+joy.leftY())*45)
		if joy.Y()==1:
			button = "Y"
			angle = str((1+joy.leftY())*45)
		if joy.B()==1:
			button = "B"
			angle = str((1+joy.leftY())*45)
		if joy.rightBumper()==1:
			button = "Z"
			angle = str((1+joy.leftY())*45)
		if joy.rightTrigger() ==1:
			button = "T"
			angle = str((1+joy.leftY())*45)

		rospy.loginfo(button+angle)
		pub.publish(button+angle)
		
		rate.sleep()
		i=i+1
	
if __name__ ==  '__main__':
	talker()