import boto3
import os

# 空ファイルを `dummy.txt` として作成する（アップロード用のダミーファイルです）
open("dummy.txt", "w").close()

# 環境変数 BUCKET_NAME からバケット名を取得する
bucket_name = os.environ["BUCKET_NAME"]

# 環境変数 REGION からリージョンを取得する
region = os.environ["REGION"]

# S3 クライアントを作成する
s3 = boto3.client('s3')

# バケットをすでに所有しているか確認し、すでに所有している場合は作成をスキップする
try:
    s3.head_bucket(Bucket=bucket_name)  # head_bucket でバケットの存在チェックを行います
    print("Bucket already exists")
except:
    print("Bucket does not exist")
    # create_bucket でバケットを region に作成します
    if region == 'us-east-1':
        s3.create_bucket(
            Bucket=bucket_name # us-east-1 の場合、CreateBucketConfiguration オプションは不要
        )
    else:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': region
            }
        )
    # バケット作成完了まで待つ（crate_bucket は非同期処理です）
    s3.get_waiter("bucket_exists").wait(Bucket=bucket_name)
    print("Bucket created")


# dummy.txt を bucket_name にアップロードする
s3.upload_file("dummy.txt", bucket_name, "dummy.txt")  # アップロードメソッドはいくつかありますが、ここではローカルファイルを指定する upload_file を使用しています
# アップロード完了まで待つ
s3.get_waiter("object_exists").wait(Bucket=bucket_name, Key="dummy.txt")
# bucket_name の中身を表示する
response = s3.list_objects_v2(Bucket=bucket_name)      # list_objects_v2 でバケット内のオブジェクトリストを取得します
for content in response["Contents"]:                   # list_objects_v2 が返したオブジェクトリストをループ処理します
    print(content["Key"])
    print(content["LastModified"])
    print(content["Size"])
# アップロードした dummy.txt を削除する
s3.delete_object(Bucket=bucket_name, Key="dummy.txt")
# 削除完了まで待つ
s3.get_waiter("object_not_exists").wait(Bucket=bucket_name, Key="dummy.txt")


# 100 MB のダミーデータを dummy2.txt として作成する
with open("dummy2.txt", "wb") as f:
    f.write(os.urandom(1024 * 1024 * 100))
    f.close()
# dummy2.txt を bucket_name にアップロードする
s3.upload_file("dummy2.txt", bucket_name, "dummy2.txt")
# アップロード完了まで待つ
s3.get_waiter("object_exists").wait(Bucket=bucket_name, Key="dummy2.txt")
# bucket_name の中身を表示する
response = s3.list_objects_v2(Bucket=bucket_name)
for content in response["Contents"]:
    print(content["Key"])
    print(content["LastModified"])
    print(content["Size"])

