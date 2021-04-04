import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import time

import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class FirebaseSender:
    def __init__(self):
        json_file_path = join(os.getcwd(), 'config', os.environ.get("FIREBASEJSONFIRENAME"))
        database_url = os.environ.get("FIREBASEADMINURL")
        cred = credentials.Certificate(json_file_path)
        firebase_admin.initialize_app(cred, {
            'databaseURL': database_url,
            'databaseAuthVariableOverride': {
                'uid': 'my-service-worker'
            }
        })
    
    def send(self, temperature, humidity, co2):
        ##databaseに初期データを追加する
        environment_ref = db.reference('/environment')

        n = datetime.datetime.now()
        time_str = n.strftime('%Y%m%d%H%M%S')
        unixtime_str = int(time.mktime(n.timetuple()))

        ref = {
            'time': unixtime_str,
            'temperature': int(temperature),
            'humidity': int(humidity),
            'co2': int(co2)
        }

        # environment_ref.set(ref)
        environment_ref.push(ref)

        ##データを取得する
        print(environment_ref.get())