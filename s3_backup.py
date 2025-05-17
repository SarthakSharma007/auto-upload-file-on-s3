import boto3


s3 = boto3.resource("s3", region_name="us-west-2")


def show_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def create_bucket(s3, bucket_name, region):
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region},
    )
    print("Bucket created successfully.")


def uplode_backup(s3, bucket_name, file_name, key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("File uploaded successfully.")


bucket_name = "my-new-bucket987455"
region = "us-west-2"
file_name = r"S:\python\python practic\backup file\backup_2025-05-03.zip"

uplode_backup(s3, bucket_name, file_name, "backup-file-.zip")

# create_bucket(s3,bucket_name,region)
# show_buckets(s3)
