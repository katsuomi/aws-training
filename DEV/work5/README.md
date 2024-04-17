# Work 5

### Work 5-1 S3 を操作してみよう (CLI)
- Lab 2 (Python) を起動し、AWS マネジメントコンソールにサインインします
- Cloud9 のページを表示して 用意された環境を開きます
- ターミナルより、以下の CLI コマンドを実行してください
- (1) バケット一覧を取得してください
  - awslabs-resources-~~~というようなバケットが返ってこれば OK です
- (2) バケットを作成してください
  - もう一度バケット一覧を取得し、作成したバケット名が表示されれば OK です
- (3) 作成したバケットのリージョンを取得してください
- (4) 作成したバケットを削除してください
  - バケット一覧を取得し、作成したバケット名が一覧から無くなっていれば OK です

### Work 5-2 S3 を操作してみよう (SDK)
- Lab 2 (Python) を起動し、AWS マネジメントコンソールにサインインします
- Cloud9 のページを表示して 用意された環境を開きます  
- メニューから "File" - "New File" を選択します
- <a href='https://github.com/katsuomi/aws-training/blob/master/DEV/work5/work5-2.py' target="_blank">work5-2.py</a> を表示して、コードをすべてコピペします
- メニューから “File” - “Save” を選択します
- "Filename" に work5-2.py と入力し、 [ Save ] をクリックします
- 下記のどちらかの手順 (手順 ① or 手順 ②) を実行してください

手順 ①: 下記の手順でステップ実行してみましょう

- ブレイクポイントを設定したい行（ここでは 1 行目の `import boto3`）の行番号の左をクリックする
  - 赤い丸がつけば OK です
- メニューから \[Run\] - \[Run Configurations\] - \[New Run Configuration\] を選択する
- 画面下部に新しいタブが表示されます (「Run Configuration」タブ)
- 「Run Configuration」タブの上部の「Command:」の横のボックスに実行したいファイル名のパスを記述する (~/environment ディレクトリからの相対パスで書きます。)  
- ここでは 「`./work5-2.py`」とします
- 環境変数を設定した状態で実行する場合は、タブ右上の `ENV` をクリックして設定します
- ここでは下記 2 つの環境変数を設定したうえで実行してください
- `BUCKET_NAME` : 他の方と重複しなさそうな名前を入力します (英数字とハイフンのみ使用)
- `REGION` : 手順画面左の `LabRegion` の値をコピペしてください
- 「Run Configuration」タブの右上部にある、**虫の絵のボタンを押してください**
  - 虫の絵の色が緑に変わります。ステップ実行可能なデバッグモードに変わったことを表します
- 「Run Configuration」タブの左上部にある緑の Run ボタン（最上部上のメニューの方ではない）を押してください
  - ブレイクポイントを設定した行で処理が一時停止し、画面右に Debugger ウィンドウが開きます
- Debugger ウィンドウで変数の内容が確認できます
- Debugger ウィンドウ内の上部にある `Run` 、 `Step Over`、 `Step Into`、`Step Out` のうち、`Step Over` ボタン <img src="https://d5yrxafrnlf73.cloudfront.net/training/step-over.png" width= "100px" /> を押して 1 行 1 行、処理内容や変数の値を確認しながら進めていってください 
  - `Run` ・・・次のブレイクポイントへ進む  
  - `Step Over` ・・・次の行へ進む  
  - `Step Into` ・・・１階層下の処理に進む  
  - `Step Out` ・・・１階層上の処理に戻る

手順 ②: 保存したコードを実行してみましょう

- まずはコードの内容を確認しましょう
- 画面下のターミナル画面を使用し、まずは環境変数を設定します
  - ```$ export BUCKET_NAME="{他の方と重複しなさそうな名前を入力します (英数字とハイフンのみ使用}"```
  - ```$ export REGION="{手順画面左の LabRegion の値をコピペしてください}"```
- コードを実行しましょう
  - ```$ python work5-2.py```
    
参考
  - 権限について  
  - 今回は、デフォルトの Cloud9 の「AWSマネージドな認証情報」が使われています
  - これは、Cloud9 を実行した IAM ユーザーまたはロール (今回は `AWSLabsUser-XXXX` というロール) の権限から IAM などの権限を除外した権限が使えます
    - (除外されない権限が[こちら](https://docs.aws.amazon.com/ja_jp/cloud9/latest/user-guide/security-iam.html#auth-and-access-control-temporary-managed-credentials-supported)にリストされています)
  - `AWSLabsUser-XXXX` というロールには S3 へのアクセス許可ポリシーが設定されています
    - ただし、本ラボの権限設定上、それを IAM コンソールから確認することはできません
