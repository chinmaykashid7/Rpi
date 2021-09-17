#! / usr / bin / python
from Adafruit_CharLCD import Adafruit_CharLCD
import time
#import commands
lcd = Adafruit_CharLCD ()
lcd.begin (16, 2)
while True:
	time = time.strftime ("% y.% b% H:% M:% S")
	temp = "vcgencmd measure_temp"
	#temp = commands.getoutput ("/ opt / vc / bin / vcgencmd measure_temp")
	lcd.message ("% s \ nCPU - Temp:% s1f"% (time, temp [5:]))
	time.sleep (5)
	lcd.home ()
