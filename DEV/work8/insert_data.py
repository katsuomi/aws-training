import boto3


# DynamoDB テーブル名を DemoTable に設定する
table_name = "DemoTable"

# DynamoDB クライアントを作成する
dynamodb = boto3.client("dynamodb")

# user_id が "user100" のデータを登録する（データサイズを 5KB 程度とする）
dynamodb.put_item(
  TableName=table_name,
  Item={
    "user_id": {"S": "user100"},
    "game_id": {"S": "game100"},
    "score": {"N": "100"},
    "data": {"B": "a"*5*1024},
  }
)
print("Data inserted successfully!")