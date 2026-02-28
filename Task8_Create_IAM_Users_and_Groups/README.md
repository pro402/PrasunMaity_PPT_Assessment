# IAM Users and Groups

Created IAM users and a user group in AWS, attached a managed policy to the group, and added users to the group to enforce access control using the IAM best practice of group-based permissions.

---

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_IAM_Group_Created.png
    └── 02_IAM_User_Permissions.png
```
---

## IAM Details

| Resource | Name |
|---|---|
| User 1 | `dev-user-1` |
| User 2 | `dev-user-2` |
| Group | `developers` |
| Policy Attached | `AmazonS3ReadOnlyAccess` (AWS Managed) |

---

## What Was Done

### Step 1 — Created IAM Users
- **IAM → Users → Create user**
- Created `dev-user-1` and `dev-user-2`
- Enabled **Console access** for both users
- Console access: **Enabled without MFA**

### Step 2 — Created IAM User Group
- **IAM → User Groups → Create group**
- Group name: `developers`
- Attached policy: **`AmazonS3ReadOnlyAccess`** (AWS managed)
- Group created successfully ✅

### Step 3 — Added Users to Group
- Opened `developers` group → **Users tab → Add users**
- Added `dev-user-1` and `dev-user-2` to the group

### Step 4 — Verified Permissions
- Opened `dev-user-1` → **Permissions tab**
- `AmazonS3ReadOnlyAccess` policy visible, **Attached via: Group `developers`** ✅

---

## Screenshots

### 01 — IAM Group Created
*Shows the `developers` user group successfully created with permissions defined (AmazonS3ReadOnlyAccess).*
![IAM Group Created](Screenshots/01_IAM_Group_Created.png)

### 02 — IAM User Permissions
*Shows `dev-user-1` with `AmazonS3ReadOnlyAccess` policy inherited via Group `developers`.*
![IAM User Permissions](Screenshots/02_IAM_User_Permissions.png)

---

## Key Concepts

| Concept | Description |
|---|---|
| IAM User | Individual identity with credentials to access AWS |
| IAM Group | Collection of users sharing the same permissions |
| IAM Policy | JSON document defining allowed/denied actions |
| AWS Managed Policy | Pre-built policy maintained by AWS |

---

## Result

`dev-user-1` and `dev-user-2` both inherit `AmazonS3ReadOnlyAccess` through the `developers` group — following the IAM best practice of **never attaching policies directly to users**, ensuring scalable and manageable access control.

