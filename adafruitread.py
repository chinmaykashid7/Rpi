from Adafruit_IO import Client

ADAFRUIT_IO_USERNAME = "chinmaykashid"
ADAFRUIT_IO_KEY = "aio_uzTw50EeIqMExkImW61EVL9H8PUX"


aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

button_feed = aio.feeds('button')

status = aio.recieve(button_feed.key).value
time.sleep(5)
