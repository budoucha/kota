# Kota version 1.20 by budoucha
Kota observes then alerts.
This application checks regularly a website and alerts on Slack when detects updates.
Currently (and for the time being) it works only with static html page (not dynamicly generated). 

## environment
Server with bash and Python3(requests, yaml and time module needed) may be sufficient.

## HOW TO USE

0. extract all files into a empty directory of your server. Using scpupload.sh may help you a bit.
1. set the parameters: edit "config.yml". Slack token can be generated [here](https://api.slack.com/docs/oauth-test-tokens)
2. run "starter.sh". You can log out from the server, Kota will continue running.


## To finish 
execute the following command "touch break" in the directory. the bot will shutdown after a while.



# にほんご
Kotaは指定したウェブページを定期的に巡回し、更新を検知したらSlackでお知らせします。
多分静的なHTMLのページじゃないと上手く動かないよ。

## 動作環境
bash、Python3(要requests, yaml, timeモジュール)が動くサーバー。

## つかいかた
- 零、　ネットにつながってるサーバーに適当なディレクトリ作ってファイル全部突っこみます。scpupload.sh使うと若干楽かも。
- 一、　"config.yml"を編集して各種パラメータを設定してね。Slackのtokenは[ここ](https://api.slack.com/docs/oauth-test-tokens)で作れるよ。
- 二、　starter.sh実行すると動き出すよ。ログアウトしても動き続けるよ。

## 終了方法
"touch break"コマンドを実行すれば巡回周期として設定した秒数以内に終了するはずだよ。
前は"ps ux"でプロセスID特定して手動でkillする必要があったんだけど、楽になったよ。やったね!


## 構成

最初から存在するファイル
- scpupload.sh: 手元のマシンからサーバーにファイルアップロードするのに使うよ。scpコマンドを実行するだけ。何なら要らない。
- chkkota.py: 本体その1。定期的にurlにアクセスして手元のhtmlと比較、差異あらばファイル"break"および"ktkr"を作成する。
- sh.sh: 本体その2、chkkota.pyを実行する、条件を満たせばループを抜けてpostMessage.pyを実行する。
- starter.sh: ログアウトしても動き続けるようsh.shをnohupで起動するする。
- config.yml: 設定用ファイル。
- postMessage.py: slackにpostするスクリプト
- readme.md: このファイルだよ！

後から作られるファイル
- ref_html：見比べる用
- break：存在すればsh.shがループから抜ける。
- ktkr：ループから抜けた時に存在していればsh.shがSlackに通知する。
- err.log: 何かエラーが起きたら書き込まれるアレ。
- out.log: chkkota.pyの実行日時とその結果が記録されているログ。
- nohup.out: なんかその他のログ的なアレ

# config.yml設定項目
"url": 見張るURL
"sleepTime": 見張る周期
"access_token": Slackのトークン 
"channel": Slackのチャンネル名、もしくはユーザー名
"message": 通知するメッセージの文面

## 更新履歴
2017/02/28
1.20
- config.txtはconfig.ymlになりました。sleepTime, access_token, channel, messageを含むようになりました。
- postMessage.pyをsh.shから分離しました。
- 特に意味は無いけど起動時にメッセージを表示するようにしました。

2016/08/20
1.1b
- scpupload.sh追加　サーバーへのアップロードが簡単にできるようになったよ

2016/08/19
1.1a　
- 実はまだ全体での動作確認できてないんだ。
- readme.txtを作ったよ。このファイルだよ
- 終了処理周りを変更したので、簡単に終了させられるようになったよ
- urlの設定を別ファイルにしたので、init.pyとchkkotaを別々に編集する必要が無くなったよ
- init.pyを追加したので、手動でhtml準備する必要が無くなったよ
- starter.shを追加したので、手動でnohupする必要が無くなったよ 

2016/08/16
1.0
- とりあえず最低限動いた


## コンゴの展望
- Slack APIの自動生成
- 全部Pythonにしたい
- requestsモジュールない環境に持ち込めたりとか出来ないかな(自動インストール)
- 任意のタイミングで終了させられるにしたい