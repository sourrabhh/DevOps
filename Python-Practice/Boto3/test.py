import boto3
import json

client = boto3.client('s3')
# response = client.create_bucket(
#     Bucket = 'souraabh-demo-bucket-001',
# )

response = client.get_bucket_acl(
    Bucket='souraabh-demo-bucket-001', 
)

# print(response)
s3_acl = json.dumps(response)

for item in s3_acl:
    if item=="Owner":
        print(s3_acl["Owner"]["DisplayName"])
# print(s3_acl["Owner"]["DisplayName"])