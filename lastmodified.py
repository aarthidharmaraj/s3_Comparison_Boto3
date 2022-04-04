import boto3

s3 = boto3.client('s3')
bucket_one_conn=boto3.client('s3',
                     aws_access_key_id = "AKIA4B5VXORR3TCWMKEE",aws_secret_access_key = "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",
                     region_name="ap-south-1")

bucket_one_bucket=bucket_one_conn.list_objects(Bucket="bucket1cmp")
objects=bucket_one_bucket["Contents"]
print(f"Total Objects: {len(objects)}\n")

print("List of all objects in that bucket\n",objects)

latest = max(objects, key=lambda x: x['LastModified'])
print("\n\nThe latest or last modified file in that bucket\n",latest)



