# Work 5-1

**Q. バケット一覧を取得してください**

A. ```$ aws s3 ls``` 

or 

A. ```$ aws s3api list-buckets```

**Q. バケットを作成してください**
 
A. ```$ aws s3 mb s3://{他の人と被らないような適当な文字列} <- バケット名になります！``` 

or  

A. ```$ aws s3api create-bucket --bucket {他の人と被らないような適当な文字列} --create-bucket-configuration LocationConstraint={ラボで指定されたリージョン}```

**Q. 作成したバケットのリージョンを取得してください**

A. ```$ aws s3api get-bucket-location --bucket {作成したバケットの名前}```

**Q. 作成したバケットを削除してください**

A.  ```$ aws s3 rb s3://{作成したバケットの名前}```

or 

A. ```$ aws s3api delete-bucket --bucket {作成したバケットの名前}```
