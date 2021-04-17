import Adafruit_DHT

import urllib.request


class AdafruitHumidityTemperatureFetcher:

    SENSOR = 22
    PIN = 4

    def __init__(self):
        pass

    def fetchData(self):
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)
            return True, {'humidity': humidity, 'temperature': temperature}
        except:
            return False, 'Adafruit DHT error'

