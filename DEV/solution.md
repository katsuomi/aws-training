# Work 3-1
### AWS CLI
**Q. aws s3 cp コマンドとはどんなコマンドですか？リファレンスをウェブ上で探してください**
**(version が 1.xx 系と 2.xx 系があります。2.xx 系を調べてください)**

A. オブジェクト（ファイル）をコピーするコマンド
https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/cp.html/

### AWS SDK
**Q. Boto3 の create_bucket の引数の情報が載っている公式の API ドキュメントを探してください**

A. https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html

# Work 5-1

**Q. バケット一覧を取得してください**

A. ```$ aws s3 ls``` 

or 

A. ```$ aws s3api list-buckets```

**Q. バケットを作成してください**
 
A. ```$ aws s3 mb s3://{他の人と被らないような適当な文字列} <- バケット名になります！``` 

or  

A. ```$ aws s3api create-bucket —bucket {他の人と被らないような適当な文字列} —region {ラボで指定されたリージョン} —create-bucket-configuration LocationConstraint={ラボで指定されたリージョン}```

**Q. 作成したバケットのリージョンを取得してください**

A. ```$ aws s3api get-bucket-location —bucket {作成したバケットの名前}```

**Q. 作成したバケットを削除してください**

A.  ```$ aws s3 rb s3://{作成したバケットの名前}```

or 

A. ```$ aws s3api delete-bucket --bucket {作成したバケットの名前}```

# Work 8-1

**Q. 以下の要件を満たすテーブルを作成してください**
 > テーブル名: Books、パーティションキー: Title、ソートキー: Volume
 > キャパシティーモード: プロビジョンド、読み込みキャパシティユニット (RCU): 5、書き込みキャパシティユニット (WCU): 5

A. ```$ aws dynamodb create-table --table-name Books --attribute-definitions AttributeName=Title,AttributeType=S AttributeName=Volume,AttributeType=N --key-schema AttributeName=Title,KeyType=HASH AttributeName=Volume,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5```

**Q. Title が「AWS Quest」、Volume が 「1」の項目を取得してください (Scan は使わないでください)**

A. ```$ aws dynamodb get-item --table-name Books --key '{"Title": {"S": "AWS Quest"}, "Volume": {"N": "1"}}'```

**Q. Title が「Cloud Story」の項目をすべて取得してください (Scan は使わないでください)**

A. ```$ aws dynamodb query --table-name Books --key-condition-expression "Title = :title" --expression-attribute-values '{":title": {"S":"Cloud Story"}}'```                                       




