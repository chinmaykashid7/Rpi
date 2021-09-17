from Adafruit_IO import Client
import RPi.GPIO as GPIO

import time
ADAFRUIT_IO_USERNAME = "chinmaykashid"
ADAFRUIT_IO_KEY = "aio_uzTw50EeIqMExkImW61EVL9H8PUX"
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN)
GPIO.setup(7,GPIO.OUT)


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

button_feed = aio.feeds('button')
count_feed = aio.feeds('count')

def led():
	if status == "ON":
		GPIO.output(7, True)
	else:
		GPIO.output(7, False)
		
	time.sleep(0.1)
countt = 0	

while 1:
	sensorvalue = GPIO.input(8)
	print(sensorvalue)
	if sensorvalue:
		print("Not detected")
	else:
		print("Detected")
		countt += 1
	aio.send(count_feed.key, str(countt))
	
	status = aio.receive(button_feed.key).value
	led()
	
