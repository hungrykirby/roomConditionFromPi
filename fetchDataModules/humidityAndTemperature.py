#!/usr/bin/python

import Adafruit_DHT

import urllib.request


class AdafruitHumidityTemperatureFetcher:

    SENSOR = 22
    PIN = 4

    def __init__(self):
        pass

    def fetchData(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)
        return {'humidity': humidity, 'temperature': temperature}

