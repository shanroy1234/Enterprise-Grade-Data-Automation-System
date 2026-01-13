import boto3
s3=boto3.client('s3')

def upload(file):
    s3.upload_file(file,'data-engine-bucket',file)
