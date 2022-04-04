
import boto3
s3 = boto3.resource('s3')
source_bucket = s3.Bucket('bucket1cmp')
destination_bucket = s3.Bucket('bucket2cmp')
source_keys= [src.key for src in source_bucket.objects.all()]
destination_keys = [dst.key for dst in destination_bucket.objects.all()]

# s3.create_bucket(Bucket='missingfiles-in-compare')
cpy=s3.Bucket('missingfiles-in-compare')
for src in source_bucket.objects.all():
    if (src.key not in destination_keys):
        copysource={"Bucket":source_bucket.name,'Key':src.key}
        cpy.copy(copysource,src.key)
        print("Missing file in bucket 1 is \t\t",src.key)
print("\n")
for dst in destination_bucket.objects.all():
    if dst.key not in source_keys:
        copysource2={"Bucket":destination_bucket.name,"Key":dst.key}
        cpy.copy(copysource2,dst.key)
        print("Missing file in bucket 2 is \t\t",dst.key)



