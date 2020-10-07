#VirtualBoxのインストールとゲストOSの起動

##VirtualBoxのインストール

[VirtualBoxのダウンロードページ](https://www.virtualbox.org/wiki/Downloads)で
Windows版6.1.14をダウンロードする。

エクスプローラ―からインストールウィザードを起動しインストールを完了させる
- Nextを押す
- Nextを押す
- Nextを押す
- Yesを押す
- Installを押す
- Finishを押す

##VirtualBoxでゲストOSの起動

仮想アプライアンスのダウンロードをする
-[仮想アプライアンスのダウンロードページ](https://8.gigafile.nu/1030-j4b8deb5d7acfa8802e95dea6db74b31e)に飛ぶ
-ダウンロードキーの右に「8510」を入力して，ダウンロード―キーをクリックする

仮想アプライアンスのインポートをする
-Oracle VM VirtualBox マネージャーから、メニューの ファイル > 仮想アプライアンスのインポートをクリックする

インポートしたい仮想アプライアンスからファイルを選択し起動する。
-インポートしたい仮想アプライアンスのファイルのイラストをクリックする
-insa2020debian.ovaを選択する
-次へをクリックする
-インポートをクリックする
-起動をクリックする

#ゲストOS上でログオンしてアプリ実行

##ゲストOSにログインする
ユーザー名「user」パスワード「wadai」を入力しLogInボタンをクリックする

ブラウザ（Firefox ESR），端末（LXTerminal）を起動する
-デスクトップ画面の左下を押すとメニューが出る
-インターネット>Firefox ESR，システムツール>LXTerminalで起動する

user@debian:~$ pwd
/home/user
user@debian:~$ cal
      10月 2020        
日 月 火 水 木 金 土  
             1  2  3  
 4  5  6  7  8  9 10  
11 12 13 14 15 16 17  
18 19 20 21 22 23 24  
25 26 27 28 29 30 31  
                      
user@debian:~$ date
2020年 10月  5日 月曜日 16:29:58 JST
user@debian:~$ date > date.txt
user@debian:~$ sudo -i
[sudo] user のパスワード:
root@debian:~# exit^C
root@debian:~# 
root@debian:~# exit
ログアウト
user@debian:~$ 

##ゲストOSでdate.txtをアップロードし、ホストOSでdate.txtを保存する
-Fireboxでmoodleにログイン
-ダッシュボード > プライベートファイルをクリックする
-メニューの横にあるファイルマネージャーをクリックしdata.txtをアップロードする
-ホストOSのブラウザでmoodleにログイン
-ダッシュボードをクリックする
-プライベートファイルよりdata.txtをダウンロードする

#C言語の復習

##Cのファイルを実行して，実行結果とプログラムコードの中身から，プログラムの内容を文章にする．

ゲストOSでCのファイルをダウンロードする
-[moodle](https://moodle2.wakayama-u.ac.jp/2020/mod/assign/view.php?id=9379)で各ファイルをクリックし、ダウンロードする

それぞれの中に書かれたコマンドを実行する


実行結果とプログラムコードの中身から，プログラムの内容を文章にする．