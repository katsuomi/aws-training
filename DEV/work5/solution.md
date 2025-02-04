# Work 5-1

**Q. バケット一覧を取得してください**

A. ```$ aws s3 ls``` 

or 

A. ```$ aws s3api list-buckets```

**Q. バケットを作成してください**
 
A. ```$ aws s3 mb s3://notes-bucket-from-cli-{ランダムな文字列} <- バケット名になります！``` 

or  

A. ```$ aws s3api create-bucket --bucket notes-bucket-from-cli-{ランダムな文字列} --region={ラボで指定されたリージョン}```

notes-bucket- から始まるバケット名でなければ、バケットの作成・削除等ができないのでご注意ください

**Q. 作成したバケットのリージョンを取得してください**

A. ```$ aws s3api get-bucket-location --bucket {作成したバケットの名前}```

ラボで us-east-1 (バージニア北部リージョン) を利用している場合、null が返ります

**Q. 作成したバケットを削除してください**

A.  ```$ aws s3 rb s3://{作成したバケットの名前}```

or 

A. ```$ aws s3api delete-bucket --bucket {作成したバケットの名前}```
