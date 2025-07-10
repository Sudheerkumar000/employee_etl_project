# Step 1: Base image
FROM python:3.11

# Step 2: Set working directory in container
WORKDIR /app

# Step 3: Copy all files to container
COPY . .

# Step 4: Install dependencies
RUN pip install pandas boto3

# Step 5: Run the ETL script
CMD ["python", "etl_script.py"]
