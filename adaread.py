import RPi.GPIO as GPIO

import time
#import f
from Adafruit_IO import Client
channel_id = 1505481
write_key = "43JQBUUQ3ETOEUBQ"


#start = 0 
#end = 0

GPIO.setmode(GPIO.BOARD)
Echo= 37
Trig = 35
LED = 33
GPIO.setup(Echo,GPIO.IN)
GPIO.setup(Trig,GPIO.OUT)
GPIO.setup(LED,GPIO.OUT)
GPIO.output(LED,False)
ADAFRUIT_IO_USERNAME = "chinmaykashid"
ADAFRUIT_IO_KEY = "aio_uzTw50EeIqMExkImW61EVL9H8PUX"

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

dist_feed = aio.feeds('dist')

def dist():
    GPIO.output(Trig, False)
    time.sleep(0.1)

    GPIO.output(Trig,True)

    time.sleep(0.00001)

    GPIO.output(Trig,False)

    while GPIO.input(Echo) == 0:
        start = time.time()

    while GPIO.input(Echo) == 1:
        end = time.time()

        Timetaken = end - start

        dist = Timetaken*17150
        dist = round(dist,2)
    return dist


#if __name__ == "__main__":
    #channel = thingspeak.Channel(id = channel_id,api_key = write_key)
    
    #print("conection done..")
while True:
    
  
    dist1 = dist()
    print(f"Measured Dist = {dist1}")
    try:
        aio.send(dist_feed.key, str(dist1))
        time.sleep(5)
    except:
        print("Exception occured..")
