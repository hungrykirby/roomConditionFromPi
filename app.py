# -*- coding: utf-8 -*-

from fetchDataModules import humidityAndTemperature
from fetchDataModules import co2
from sendData import firebase

def main():
    ht = humidityAndTemperature.AdafruitHumidityTemperatureFetcher().fetchData()
    humidity = ht['humidity']
    temperature = ht['temperature']

    result, value = co2.MHZ19CO2Fetcher().fetchData()
    if result and int(temperature) < 50 and int(humidity) < 100:
        sender = firebase.FirebaseSender()
        sender.send(temperature, humidity, value)
    else:
        print('Error')

if __name__ == '__main__':
    main()
