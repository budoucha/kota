# Kota version 1.1b by budoucha

A bot that checks regularly a website and alerts on Slack when detects updates.
Currently it works only with static html page (not dynamicly generated). 

## environment
Server with bash and Python3(with requests module) may be sufficient.

## HOW TO USE

0. extract all files into a working directory of your server. Using scpupload.sh may help you a bit.
1. set the URL of the web page to check: edit "config.txt".
2. prepare html to compare: run "init.py".
3. set your alerting Slack API: edit sh.sh, replace the URL of the curl line with your alerting API(provided here https://api.slack.com/methods/chat.postMessage/test )
4. run "starter.sh". You can log out from the server, the bot will continue running.


## To finish 
do "touch break" in the directory. the bot will shutdown in maximum 300 seconds.



# 英語苦手？
なんか指定したウェブページが更新されるまで定期巡回して更新されたらSlackで知らせてくれるbotみたいなもんだよ。
多分静的なHTMLのページじゃないと多分上手く動かないよ。

## 動作環境
bash、Python3(含むrequestsモジュール)が動けばいけるはず。

## つかいかた
- 零、　ネットにつながってるサーバーに適当なディレクトリ作ってファイル全部突っこむんだよ。scpupload.sh使うと若干楽かも
- 一、　"config.txt"を編集して粘着したいサイトのURL書き込んでね。
- 二、　比較用のhtml用意するからinit.pyを実行してね。
- 三、　sh.shを編集して通知用のSlack APIを適当に設定してね。詳しくはここ見てね。　https://api.slack.com/methods/chat.postMessage/test
- 四、　starter.sh実行すると動き出すよ。

## 終了方法
"touch break"コマンドを実行すれば300秒以内に終了するはずだよ。
前は"ps ux"でプロセスID特定して手動でkillする必要があったんだけど、楽になったよ。やったね!


## 構成

最初から存在するファイル
- scpupload.sh: 手元のマシンからサーバーにファイルアップロードするのに使うよ。scpコマンドを実行するの。
- chkkota.py：本体その1。urlにアクセスして手元のhtmlと比較、差異あらばファイル"break"および"ktkr"を作成する。
- sh.sh：本体その2、5分おきにchkkota.pyを実行、条件を満たせばループを抜けてSlackに通知する。
- starter.sh：ログアウトしても動き続けるようsh.shをnohupで起動するする。
- config.txt：url設定用のファイル。その内他の設定もここに集約したい(願望)。


後から作られるファイル
- html：見比べる用のhtmlファイル
- break：存在すればsh.shがループから抜ける。
- ktkr：ループから抜けた時に存在していればsh.shがSlackに通知する。
- out.log：chkkota.pyの実行日時とその結果が記録されているログ。
- nohup.out、err.log：なんかそういうアレ


## 更新履歴
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
- config.txtの複数項目対応、Pythonからの参照方法を工夫
- sh.shからconfig.txtを参照できるようにしたい
- sleep時間とSlack APIをsh.shからconfig.txtに移行
- Slack APIの自動生成
- てか全部Pythonにしたい
- requestsモジュールない環境に持ち込めたりとか出来ないかな