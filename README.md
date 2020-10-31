<div align="center"><img src="https://tsukukoma-streetview.site/static/streetview/images/streetview-top.jpg" width="400"/></div>

# Tsukukoma Street View：360度カメラだけでストリートビュー
[**Tsukukoma Street View**](https://tsukukoma-streetview.site/)

[**Twitter**](https://twitter.com/69th_ennichi)

## インストール
Tsukukoma Street View を使う前にpipでPythonとDjangoとPillowをインストールしてください。
```sh
$ pip install python, django, pillow
```

## サーバーを実行
初めて実行するときはまず
```sh
$ python manage.py migrate
```
してください。

実行は以下のコマンドでできます。
```sh
$ python manage.py runserver
```
「[http://127.0.0.1:8000/](http://127.0.0.1:8000/)」に入ります

## 管理者サイトにログイン
まず管理者を追加します。
```sh
$ python manage.py createsuperuser
```
これをすると、ユーザー名、メールアドレス（空欄可）、パスワードを入力するように言われます。

このアカウントで「[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/)」にログインします。

## シーンの追加
「ホーム＞Streetview＞シーン＞シーンを追加」から設定します。

画像の初期方向は、全ての画像が画面をロードした時の向きがに現実空間において同じ方向になるよう（例えば南とか）に設定するとうまくいきます。
時計回りが正で度数法で表します。

RelatedSceneの「画像の初期方向」は無視してください（シーンをリンクで切り替える場合は必要になります）
隣の画像に行くためのボタンの位置は極座標で表します。「THETA」はSceneの初期方向からの回転角です。
ボタンのサイズはRを大きくし過ぎてしまったときに変更してください。

## カメラ
私たちはRicoh社の[**RICOH THETA SC**](https://theta360.com/ja/about/theta/sc.html)というカメラ（2万円ほど）を使いました。
5376×2688ピクセルで撮影しましたが、これより低い解像度だとパノラマビューで見たときに気持ち悪くなってしまうので、これが限度でしょう。

## 本番環境での実行
Djangoを使うのであればVPSかクラウドサーバーです。
[**こちらのサイト**](https://hombre-nuevo.com/vps/vps0001/)が参考になります。情報が古いのか、少し間違っているところがありますが、これ以上分かりやすいサイトはないと思います。

ちなみに私たちの環境はこんな感じです。
```sh
CentOS 7.8
Apache 2.4.6
Python 3.6.4
Django==3.1.2
mod-wsgi==4.7.1
mysqlclient==2.0.1
Pillow==8.0.0
```
```
