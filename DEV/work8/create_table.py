import boto3


# DynamoDB テーブル名を DemoTable に設定する
table_name = "DemoTable"

# DynamoDB クライアントを作成する
dynamodb = boto3.client("dynamodb")

# DynamoDB テーブルを作成する
# テーブルのキーは user_id と game_id を指定する
dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {"AttributeName": "user_id", "KeyType": "HASH"},
        {"AttributeName": "game_id", "KeyType": "RANGE"},
    ],
    AttributeDefinitions=[
        {"AttributeName": "user_id", "AttributeType": "S"},
        {"AttributeName": "game_id", "AttributeType": "S"},
    ],
    ProvisionedThroughput={"ReadCapacityUnits": 1, "WriteCapacityUnits": 5},
)
# テーブル作成完了を待つ
dynamodb.get_waiter("table_exists").wait(TableName=table_name)
print("Table created successfully!")