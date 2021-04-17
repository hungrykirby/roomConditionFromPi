import Adafruit_DHT

import urllib.request


class AdafruitHumidityTemperatureFetcher:

    SENSOR = 22
    PIN = 4

    def __init__(self):
        pass

    def fetchData(self):
        # return bool, object or string
        # bool: 実行結果。Falseのときは正しく湿度と気温を取得できたはず
        # object: {'humidity': 湿度の値, 'temperature': 温度の値}
        # str: エラー文言。特に意味はない
        try:
            humidity, temperature = Adafruit_DHT.read_retry(self.SENSOR, self.PIN)
            if self.__valid_value(humidity, temperature):
                return True, {'humidity': humidity, 'temperature': temperature}
            return False, 'Range error'
        except:
            return False, 'Adafruit DHT error'

    def __valid_value(self, humidity, temperature):
        # 湿度が100%以上や温度60度以上もしくは-30度以下が取得された場合
        # おかしい値が取得されている気がするのでFalseを返す
        if humidity > 100:
            return False
        elif temperature > 60 or temperature < -30:
            return False
        else:
            return True

