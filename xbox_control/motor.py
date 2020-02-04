from adafruit_servokit import ServoKit
import time
import argparse
parser = argparse.ArgumentParser(description=' Angle joystick left')
parser.add_argument("--a")
parser.add_argument("--b")
parser.add_argument("--t")
args = parser.parse_args()

robot= ServoKit(channels=16)
if args.b == "A":
	robot.servo[0].angle = float(args.a)
if args.b == "X":
	robot.servo[1].angle = float(args.a)
if args.b == "Y":
	robot.servo[2].angle = float(args.a)
if args.b == "B":
	robot.servo[3].angle = float(args.a)
if args.b == "Z":
	robot.servo[4].angle = float(args.a)
if args.b == "T":
	robot.servo[0].angle = float(args.a)
	robot.servo[1].angle = float(args.a)
	robot.servo[2].angle = float(args.a)
	robot.servo[3].angle = float(args.a)
	robot.servo[4].angle = float(args.a)