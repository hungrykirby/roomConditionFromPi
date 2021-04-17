# roomConditionFromPi
室内環境をらずぱいで取得してfirebaseのRealtimeDatabaseに送信します。

## 確認した動作環境

- Raspberry Pi 3
- Raspberry Pi 3+
- python 3.7.3
    - python 3.9ではfirebase adminが入らなかった

## 必要なモジュール

`pip install firebase-admin`

firebase admin sdk

らずぱいと相性が悪いのか入らなかったという記事が多い。バージョンを下げたら動いた。

***

`pip install python-dotenv`

環境変数を使えるようにする

***

`mh_z19`

pyenvを使っているのだが、
> MH-Z19センサーはシリアル通信を利用して読み込むため、デフォルトの設定ではroot権限が必要になる

らしく強引に入れてsubprocessで動かしている。

`sudo pip install mh-z19` 

[参考記事](https://dev.classmethod.jp/articles/raspberry-pi-4-b-mh-z19b-co2/)

***

`Adafruit_DHT`

単純には入らなかったので[Qiita](https://qiita.com/kelvin27315/items/fc33bae33c9e78b720a9)を参考にがんばって入れる必要がある。

## ハードウェア

頑張る

## 環境変数

`cp .env.sample .env` として記載。

`config/` に[公式サイト](https://firebase.google.com/docs/admin/setup?hl=ja)を参考にfirebase admin用のキーを含むjsonファイルを置いて、そのファイル名を

`FIREBASE_FIRENAME` に記載する。

`FIREBASE_ADMINURL` はfirebaseのRealtime DatabaseのURL。`https://<DATABASE_NAME>.firebaseio.com` となるはず。