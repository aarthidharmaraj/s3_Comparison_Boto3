import boto3, json


bucket_conn=boto3.client('s3',
                     aws_access_key_id = "****",aws_secret_access_key = "****",
                     region_name="ap-south-1")
          
bucket_one_bucket=bucket_conn.list_objects(Bucket="bucket1cmp")
objects1=bucket_one_bucket.get("Contents")
print(f"Total Objects: {len(objects1)}\n")

print("List of all objects in the bucket1cmp \n",objects1)

bucket_two_bucket=bucket_conn.list_objects(Bucket="bucket2cmp")
objects2=bucket_two_bucket.get("Contents")
print(f"Total Objects: {len(objects2)}\n")

print("List of all objects in the bucket2cmp\n",objects2)

# #For comparing with keys and check it exixts in another bucket
# print("\nThe objects with their Keys in bucket1cmp\n")
# for keyobj1 in objects1:
#     print(keyobj1)
# print("\nThe objects with their Keys in bucket2cmp\n")
# for keyobj2 in objects2:
#     print(keyobj2)
samefiles=[]
missingfiles1=[]
missingfiles2=[]
for keyobj1 in objects1:

    for keyobj2 in objects2:
        if keyobj1['Key'] == keyobj2['Key']:
            samefiles.append(keyobj1['Key'])
            # print(samefiles)
            flag=1
        flaf=0
        missingfiles2.append(keyobj2['Key'])
    missingfiles1.append(keyobj1['Key'])

print("\nSame files\t\t",samefiles)
newmissingfiles1=set(missingfiles1)-set(samefiles)
print("\nmissingfiles in bucket 1\t\t",newmissingfiles1)
newmissingfiles2=set(missingfiles2)-set(samefiles)
# missingfiles2 = list(dict.fromkeys(missingfiles2))
print("\nmissingfiles in bucket 2\t\t",newmissingfiles2)

if flag==1:
    print("\nThe files are present in both buckets")
    print("\nThe files present in both buckets are",samefiles)
else:
    print("\nThe missing files in bucket 1 are",newmissingfiles1)
    print("\nThe missing files in bucket 2 are",newmissingfiles2)
    

    