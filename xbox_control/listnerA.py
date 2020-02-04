import rospy
from std_msgs.msg import String
import subprocess
import argparse

button = "0"
angle= "0"
def chatter_callback(message):
	rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)
	button = message.data[0:1]
	angle = message.data.lstrip(message.data[:1])
	print(button)
	print(angle)
	subprocess.call(["sudo","python3","motor.py","--a",angle,"--b",button])

def listener():
	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber("Buttons", String, chatter_callback)
	rospy.spin()
	
if __name__ == '__main__':
	listener()
