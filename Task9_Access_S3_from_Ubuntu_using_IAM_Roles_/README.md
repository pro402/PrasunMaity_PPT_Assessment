# Access S3 from EC2 using IAM Role

Attached an IAM Role to an EC2 instance to securely access S3 without using access keys.

---

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_IAM_Role_Created.png
    └── 02_S3_Access_Terminal.png
```
---

## IAM & EC2 Details

| Field | Value |
|---|---|
| IAM Role | `s3Role` |
| Policy Attached | `AmazonS3ReadOnlyAccess` |
| EC2 Instance | `s3RoledEc2` (`i-060fd132710f6637c`) |
| Region | `us-east-1` |

---

## What Was Done

### Step 1 — Created IAM Role
- **IAM → Roles → Create role**
- Trusted entity: **AWS service → EC2**
- Policy attached: **`AmazonS3ReadOnlyAccess`**
- Role name: `s3Role`

### Step 2 — Attached Role to EC2
- **EC2 → Instances → `s3RoledEc2`**
- **Actions → Security → Modify IAM role → `s3Role`** → Update

### Step 3 — Installed AWS CLI on EC2
```bash
sudo snap install aws-cli --classic
aws --version
# aws-cli/2.34.0 Python/3.13.11 Linux/6.14.0-1018-aws
```

### Step 4 — Verified Role & Accessed S3
```bash
aws sts get-caller-identity
```
```json
{
    "UserId": "AROAS4IFQ5THS6NZU3LHZ:i-060fd132710f6637c",
    "Account": "198116961487",
    "Arn": "arn:aws:sts::198116961487:assumed-role/s3Role/i-060fd132710f6637c"
}
```
```bash
aws s3 ls
# 2026-02-28 15:28:28 newbycket43434
```

---

## Screenshots

### 01 — IAM Role Created
*Shows `s3Role` with `AmazonS3ReadOnlyAccess` policy attached, trusted entity: EC2.*
![IAM Role Created](Screenshots/01_IAM_Role_Created.png)

### 02 — S3 Access from Terminal
*Shows `aws sts get-caller-identity` confirming access via `assumed-role/s3Role`, and `aws s3 ls` listing the S3 bucket — no access keys used.*
![S3 Access Terminal](Screenshots/02_S3_Access_Terminal.png)

---

## Result

EC2 instance `s3RoledEc2` successfully accessed S3 using the attached IAM Role — confirmed by `assumed-role/s3Role` in the ARN. **No access keys or `aws configure` were needed**, demonstrating secure role-based access.

