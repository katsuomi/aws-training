# Work 8-1

**Q. 以下の要件を満たすテーブルを作成してください**
 > テーブル名: Books、パーティションキー: Title、ソートキー: Volume
 > キャパシティーモード: プロビジョンド、読み込みキャパシティユニット (RCU): 5、書き込みキャパシティユニット (WCU): 5

A. ```$ aws dynamodb create-table --table-name Books --attribute-definitions AttributeName=Title,AttributeType=S AttributeName=Volume,AttributeType=N --key-schema AttributeName=Title,KeyType=HASH AttributeName=Volume,KeyType=RANGE --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5```

**Q. Title が「AWS Quest」、Volume が 「1」の項目を取得してください (Scan は使わないでください)**

A. ```$ aws dynamodb get-item --table-name Books --key '{"Title": {"S": "AWS Quest"}, "Volume": {"N": "1"}}'```

**Q. Title が「Cloud Story」の項目をすべて取得してください (Scan は使わないでください)**

A. ```$ aws dynamodb query --table-name Books --key-condition-expression "Title = :title" --expression-attribute-values '{":title": {"S":"Cloud Story"}}'```                                       
