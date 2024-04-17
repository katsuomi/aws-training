### Work 3-1 ドキュメントを確認してみよう
- AWS CLI
  - aws s3 cp コマンドとはどんなコマンドですか？リファレンスをウェブ上で探してください
    - (version が 1.xx 系と 2.xx 系があります。2.xx 系を調べてください)
- AWS SDK
  - Boto3 の create_bucket の引数の情報が載っている公式の API ドキュメントを探してください

### Work 3-2 Cloud9 を使ってみよう
- Lab 1 (Python) を起動し、AWS マネジメントコンソールにサインインします
- Cloud9 のページを表示して用意された環境を開きます
- メニューから "File" - "New File" を選択します
- 以下のコードをコピペします
```
# 現在日時を取得して表示する
import datetime

dt_now = datetime.datetime.now()
print(dt_now)
```
- メニューから “File” - “Save” を選択します
- "Filename" に work3-2.py と入力し、 [ Save ] をクリックします
- 画面下のターミナル画面を使用し、以下のように実行します
```
python work3-2.py
```
- 実行した日時 (日本時間 – 9 時間) が返ってきたら OK です
