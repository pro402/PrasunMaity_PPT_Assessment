# Task 5 — Serverless + Event-Driven Architecture (AWS)

## Objective

Implement an event-driven serverless architecture on AWS where an S3 file upload automatically triggers a Lambda function that stores metadata into DynamoDB, with CloudWatch monitoring enabled.

---

## Architecture Overview

```
User uploads file
      │
      ▼
  S3 Bucket  ──── S3 Event Trigger ────▶  Lambda Function
(task5-bucket)                            (task5-lambda)
                                               │
                                               ▼
                                          DynamoDB Table
                                          (task5-table)
                                               │
                                               ▼
                                          CloudWatch Logs
```

---

## AWS Services Used

| Service     | Purpose                                      |
|-------------|----------------------------------------------|
| S3          | Object storage — triggers on file upload     |
| Lambda      | Serverless compute — processes the event     |
| DynamoDB    | NoSQL database — stores file metadata        |
| IAM         | Role and permissions for Lambda              |
| CloudWatch  | Logs and monitoring for Lambda execution     |

---

## Step-by-Step Implementation

### Step 1 — Create S3 Bucket

1. Go to **AWS Console → S3 → Create bucket**
2. Bucket name: `task5-bucket-prasun` (must be globally unique)
3. Region: `us-east-1`
4. Block all public access: ✅ Enabled
5. Click **Create bucket**

---

### Step 2 — Create DynamoDB Table

1. Go to **AWS Console → DynamoDB → Create table**
2. Table name: `task5-table`
3. Partition key: `fileName` (String)
4. Table settings: Default (On-demand capacity)
5. Click **Create table**

---

### Step 3 — Create IAM Role for Lambda

1. Go to **IAM → Roles → Create role**
2. Trusted entity: **AWS Service → Lambda**
3. Attach these policies:
   - `AmazonS3ReadOnlyAccess`
   - `AmazonDynamoDBFullAccess`
   - `CloudWatchLogsFullAccess`
4. Role name: `task5-lambda-role`
5. Click **Create role**

---

### Step 4 — Create Lambda Function

1. Go to **AWS Console → Lambda → Create function**
2. Function name: `task5-lambda`
3. Runtime: `Python 3.12`
4. Execution role: **Use existing role → `task5-lambda-role`**
5. Click **Create function**

Replace the default code with:

```python
import json
import boto3
import urllib.parse
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('task5-table')

def lambda_handler(event, context):
    record = event['Records']
    bucket = record['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(record['s3']['object']['key'])
    size = record['s3']['object']['size']
    timestamp = datetime.utcnow().isoformat()

    table.put_item(Item={
        'fileName': key,
        'bucketName': bucket,
        'fileSize': str(size),
        'uploadedAt': timestamp
    })

    print(f"Stored: {key} from {bucket} at {timestamp}")
    return {'statusCode': 200, 'body': json.dumps('Success')}
```

6. Click **Deploy**

---

### Step 5 — Configure S3 Upload Trigger

1. In Lambda → **Function overview → Add trigger**
2. Select **S3**
3. Bucket: `task5-bucket-prasun`
4. Event type: **PUT** (or `All object create events`)
5. Acknowledge recursive invocation warning ✅
6. Click **Add**

---

### Step 6 — Enable CloudWatch Logs

CloudWatch Logs are automatically created when Lambda runs. To verify:

1. Go to **CloudWatch → Log groups**
2. Find: `/aws/lambda/task5-lambda`
3. Open the log stream after a test invocation

To create a CloudWatch Alarm:
1. **CloudWatch → Alarms → Create alarm**
2. Metric: **Lambda → By Function Name → `task5-lambda` → Errors**
3. Threshold: `>= 1` error
4. Notification: SNS (optional)

---

### Step 7 — Test the Pipeline

1. Go to **S3 → `task5-bucket-prasun` → Upload**
2. Upload any file (e.g., `test.txt`)
3. Verify in **DynamoDB → `task5-table` → Explore items** — new entry should appear
4. Verify in **CloudWatch → Log groups → `/aws/lambda/task5-lambda`** — log entry confirms execution

---
## Resources Created

| Resource         | Name                    | Region    |
|------------------|-------------------------|-----------|
| S3 Bucket        | `task5-bucket-prasun`   | us-east-1 |
| Lambda Function  | `task5-lambda`          | us-east-1 |
| DynamoDB Table   | `task5-table`           | us-east-1 |
| IAM Role         | `task5-lambda-role`     | Global    |
| CloudWatch Group | `/aws/lambda/task5-lambda` | us-east-1 |
