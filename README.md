# util-py
日常生活で使う小さな Python コードの置き場

## Auto Click GUI(USSR) の使い方
![Auto Click GUI を使用している画面の写真](./auto_click_gui_image.png "Auto Click GUI を使用している画面の写真")

環境構築等は不要、/auto/auto_click_gui 直下にある SovietAutoClicker.exe を実行してください。

## Get Youtube Audio GUI の使い方
![Get Youtube Audio GUI を使用している画面の写真](./get_youtube_audio_gui_image.png "Get Youtube Audio GUI を使用している画面の写真")

YouTube 上から音源を取得する GUI

※ 事前に ffmpeg を導入してから GUI を起動してください。

### Usage
/youtube 直下にある get_youtube_audio_gui.exe を実行してください。

1. URL と保存名を入力します。
1. MP3 か M4R のダウンロードボタンを押せば完了です。

## get_m4r.py の使い方
音源を m4r で取得する書き捨てコード

※ 事前に ffmpeg を導入してください。

```sh
git clone https://github.com/Ant2357/util-py.git
cd util-py

# 説明簡略化の為に書いてないけど、基本は venv 等を使ってください
pip install -r requirements.txt

cd youtube
python get_m4r.py
```
