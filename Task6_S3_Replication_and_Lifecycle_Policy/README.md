# S3 Replication & Lifecycle Policy

Configured Cross-Region Replication (CRR) between two S3 buckets across different AWS regions, and applied a Lifecycle Policy to automate storage class transitions and object expiration for cost optimization.

---

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_Two_Buckets_Created.png
    ├── 02_Source_Bucket_Objects.png
    ├── 03_Batch_Replication_Job.png
    ├── 04_Destination_Bucket_Replicated.png
    ├── 05_Lifecycle_Rule_Preview.png
    └── 06_Lifecycle_Rule_Enabled.png
```
---

## Bucket Details

| Role | Bucket Name | Region |
|---|---|---|
| Source | `prasunmainbucket01` | `us-east-1` (N. Virginia) |
| Destination | `prasundestinationbucket02` | `us-west-2` (Oregon) |

---

## Part 1: Cross-Region Replication (CRR)

### Step 1 — Created Two Buckets
- `prasunmainbucket01` in `us-east-1`
- `prasundestinationbucket02` in `us-west-2`
- **Versioning enabled** on both buckets (required for replication)

### Step 2 — Configured Replication Rule
- Source bucket → **Management** tab → **Replication rules** → **Create rule**
- Rule name: `replicate-all`
- Scope: Entire bucket
- Destination: `prasundestinationbucket02`
- IAM Role: Auto-created by AWS

### Step 3 — Replicated Existing Objects (Batch Operations)
- Selected **Yes** to replicate existing objects → AWS created a **Batch Operations job**
- Job ID: `b011ed0f-7a50-4ef0-babe-38fdb3fc7c0f`
- Job settings: **Automatically run when ready**, completion report to source bucket
- Result: **9 objects replicated, 100% complete, 0 failed**

### Step 4 — Verified Replication
- Opened `prasundestinationbucket02` (us-west-2)
- Confirmed all **10 objects** (9 files + 1 batch job report folder) are present ✅

---

## Part 2: Lifecycle Policy

### Rule Name: `move-to-glacier`
- Scope: Entire bucket (`prasunmainbucket01`)
- Status: **Enabled**

### Transition & Expiration Actions

**Current Version Actions**

| Day | Action |
|---|---|
| Day 0 | Objects uploaded |
| Day 30 | Transition to **Standard-IA** |
| Day 60 | Transition to **Glacier Instant Retrieval** |
| Day 90 | **Objects expire (deleted)** |

**Noncurrent Version Actions**

| Day | Action |
|---|---|
| Day 0 | Versions become noncurrent |
| Day 30 | 3 newest retained → rest move to **Standard-IA** |
| Day 75 | 3 newest retained → rest move to **Glacier Instant Retrieval** |

---

## Screenshots

### 01 — Two Buckets Created
*Shows both `prasunmainbucket01` (us-east-1) and `prasundestinationbucket02` (us-west-2) listed in S3.*
![Two Buckets Created](Screenshots/01_Two_Buckets_Created.png)

### 02 — Source Bucket Objects
*Shows all 10 objects in `prasunmainbucket01` with versioning enabled.*
![Source Bucket Objects](Screenshots/02_Source_Bucket_Objects.png)

### 03 — Batch Replication Job
*Shows the Batch Operations job at 100% completion — 9 objects replicated, 0 failed.*
![Batch Replication Job](Screenshots/03_Batch_Replication_Job.png)

### 04 — Destination Bucket Replicated
*Shows `prasundestinationbucket02` (us-west-2) with all 10 objects successfully replicated.*
![Destination Bucket Replicated](Screenshots/04_Destination_Bucket_Replicated.png)

### 05 — Lifecycle Rule Preview
*Shows the full transition and expiration timeline before rule creation.*
![Lifecycle Rule Preview](Screenshots/05_Lifecycle_Rule_Preview.png)

### 06 — Lifecycle Rule Enabled
*Shows the `move-to-glacier` lifecycle rule active under Lifecycle configuration of `prasunmainbucket01`.*
![Lifecycle Rule Enabled](Screenshots/06_Lifecycle_Rule_Enabled.png)

---

## Result

- All **9 objects** from `prasunmainbucket01` (us-east-1) were successfully replicated to `prasundestinationbucket02` (us-west-2) via S3 Batch Operations with **0 failures**.
- Lifecycle rule `move-to-glacier` is **active**, automating cost optimization by progressively moving objects to cheaper storage tiers and expiring them at Day 90.
