import pandas as pd
import boto3
import os
# Step 1: Read raw data
df = pd.read_csv("employees_raw.csv")
print("Original Data:\n", df)

# Step 2: Add 'status' column
df['status'] = df['salary'].apply(lambda x: 'High' if x >= 70000 else 'Normal')
print("\nTransformed Data:\n", df)

# Step 3: Save to new file
df.to_csv("employees_cleaned.csv", index=False)
print("\n✅ Cleaned file saved successfully!")

# AWS credentials (for testing only – don't hardcode in production)

aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

bucket_name = 'employee-etl-2025-sudheer'  # like sudheer-etl-bucket
s3_key = 'output/employees_cleaned.csv'

# Connect to AWS S3
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name='us-east-1'
)

# Upload the file
with open("employees_cleaned.csv", "rb") as f:
    s3.upload_fileobj(f, bucket_name, s3_key)

print("✅ File uploaded to S3 successfully!")
