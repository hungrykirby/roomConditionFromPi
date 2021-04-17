# -*- coding: utf-8 -*-

from fetchDataModules import humidityAndTemperature
from fetchDataModules import co2
from sendData import firebase

def main():
    result_ht, ht = humidityAndTemperature.AdafruitHumidityTemperatureFetcher().fetchData()

    result_co2, value = co2.MHZ19CO2Fetcher().fetchData()
    
    # 湿度、温度、二酸化炭素濃度がいずれかただしく取得できなかったら送信しない
    if result_ht and result_co2:
        humidity = ht['humidity']
        temperature = ht['temperature']
        sender = firebase.FirebaseSender()
        sender.send(temperature, humidity, value)
    else:
        print('Error')

if __name__ == '__main__':
    main()
