import pandas as pd
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Step 1: Read raw data
df = pd.read_csv("employees_raw.csv")
print("Original Data:\n", df)

# Step 2: Add 'status' column
df['status'] = df['salary'].apply(lambda x: 'High' if x >= 70000 else 'Normal')
print("\nTransformed Data:\n", df)

# Step 3: Save to new file
df.to_csv("employees_cleaned.csv", index=False)
print("\n✅ Cleaned file saved successfully!")

# Step 4: AWS credentials from .env
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')

# Step 5: Upload to S3
bucket_name = 'employee-etl-2025-sudheer'
s3_key = 'output/employees_cleaned.csv'
s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='us-east-1'
)

with open("employees_cleaned.csv", "rb") as f:
    s3.upload_fileobj(f, bucket_name, s3_key)
