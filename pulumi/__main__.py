import pulumi
import pulumi_aws as aws

# Create an S3 bucket
example_bucket = aws.s3.Bucket("exampleBucket",
    bucket="example-bucket",
    acl="private"
)

# Export the bucket name
pulumi.export("bucket_name", example_bucket.bucket)