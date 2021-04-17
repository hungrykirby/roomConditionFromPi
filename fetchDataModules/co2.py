import subprocess
import re

class MHZ19CO2Fetcher:
    def __init__(self):
        pass

    def fetchData(self):
        # return Bool, str or int
        # Bool: 実行結果。Falseはなんらかのエラーまたは不正な値が来た
        # str or int: BoolがFalseのときにはエラー内容の文字列が返る
        # TODO: エラーオブジェクトで返すようにする。
        # Trueのときには二酸化炭素濃度の数値が返る
        try:
            out = subprocess.check_output(['sudo', 'python', '-m', 'mh_z19'])
            # outには {"co2": 1234} みたいな文字列が返ってくる
            value = self.__extractCO2FromOutput(out)
            if not value:
                return False, 'Not Found Matched Int'
            return True, value
        except:
            return False, 'subprocess error'

    def __extractCO2FromOutput(self, out):
        # return Int or False
        # {"co2": 1234} こんな感じの文字列から数字列（二酸化炭素濃度の値）
        # を取得する
        # matchできないなどの理由で取得できない場合はFalseを返す
        # たまに「新しいメールが /var/mail/pi にあります」みたいな文字列も一緒に来ることがあるため
        # 改行で分割して最初の要素を抽出
        try:
            d = out.decode().strip().split('\n')[0]
            pattern = '{"co2": (\d+)}'
            result = re.match(pattern, d)
            if not result:
                return False
            return int(result.group(1))
        except:
            return False