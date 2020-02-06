from adafruit_servokit import ServoKit
from flask import Flask
import time
import sys
from flask import render_template
app = Flask(__name__)

@app.route("/")
def une_fonction():
	return render_template("index.html")

@app.route("/Bouton1")
def une1_fonction():
	robot = ServoKit(channels=16)
	robot.servo[12].angle = 0
	time.sleep(1)
	robot.servo[12].angle = 180
	time.sleep(1)
	robot.servo[12].angle = 0
	time.sleep(1)
	return render_template("index.html")

	return "string"

@app.route("/Bouton2")
def une2_fonction():
	robot = ServoKit(channels=16)
	robot.servo[12].angle = 0
	time.sleep(1)
	robot.servo[12].angle =  90
	time.sleep(1)
	robot.servo[12].angle = 0
	time.sleep(1)
	return render_template("index.html")

	return "string"

@app.route("/Entrer")
@app.route("/Entrer/<moteur>/<angle1>")
def une3_fonction(angle1=None, moteur=None):
	robot = ServoKit(channels=16)
	robot.servo[int(moteur)].angle = int(angle1)
	time.sleep(1)
	return render_template("index.html")

	return "string"

if __name__ == "__main__":
	app.run(host='0.0.0.0')




