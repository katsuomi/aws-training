import boto3
from botocore.client import Config

# DynamoDB テーブル名を DemoTable に設定する
table_name = "DemoTable"

# DynamoDB クライアントを作成する
config = Config(
    retries=dict(
        max_attempts=0
    )
)
dynamodb = boto3.client("dynamodb", config=config)

# user_id が "user100" のデータを取得する
response = dynamodb.query(
  TableName=table_name,
  KeyConditionExpression="user_id = :user_id",
  ExpressionAttributeValues={":user_id": {"S": "user100"}},
  ScanIndexForward=False,
  ConsistentRead=True,
  ReturnConsumedCapacity='TOTAL',
)