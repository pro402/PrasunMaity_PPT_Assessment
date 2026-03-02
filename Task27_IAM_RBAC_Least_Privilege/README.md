# IAM + RBAC + Least Privilege (AWS + Azure)

## Project Structure
```
Task3-IAM-RBAC/
├── README.md
├── AWS/
      ├── deny-s3-delete-policy.json
      └── Screenshots/
          ├── 01_aws_iam_user_developer.png
          ├── 02_aws_ec2_policy_attached.png
          ├── 03_aws_custom_deny_s3_policy.png
          ├── 04_aws_iam_role_policy_attached.png
          ├── 05_aws_ec2_access_success.png
          └── 06_aws_s3_delete_denied.png
    └── Azure/
    ├── notes.md
    └── Screenshots/
        ├── 07_azure_entra_user_created.png
        ├── 08_azure_reader_role_rg.png
        ├── 09_azure_contributor_role_vm.png
        ├── 10_azure_allowed_action.png
        └── 11_azure_restricted_action.png
```

## What Was Done
1. Created IAM user `Developer` with console access in AWS IAM
2. Attached `AmazonEC2FullAccess` + `AmazonS3ReadOnlyAccess` for minimum required permissions
3. Created custom `DenyS3DeletePolicy` (JSON) — explicitly blocks `s3:DeleteObject` and `s3:DeleteBucket`
4. Attached deny policy via `DeveloperRole` and directly to user — EC2 works, S3 delete blocked ✅
5. Created user `Developer` in Microsoft Entra ID
6. Assigned **Reader** on `task3-rg` (view only) and **Contributor** on `task3-rg-vm` (manage that VM only)
7. Verified: VM management allowed, resource deletion denied with authorization error ✅

## Key Concepts

| Concept | Description |
|---|---|
| Explicit Deny | In AWS, Deny always overrides Allow regardless of other policies |
| Least Privilege | Grant only the minimum permissions needed — nothing more |
| Azure RBAC Scope | Roles assigned at RG level apply broadly; narrower resource-level roles can elevate specific access |
| Reader | View-only Azure role — no create, modify, or delete |
| Contributor | Full resource management in Azure — cannot assign roles or delete RG |

## AWS Policy Used
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyS3Delete",
      "Effect": "Deny",
      "Action": ["s3:DeleteObject", "s3:DeleteBucket"],
      "Resource": "*"
    }
  ]
}
```
