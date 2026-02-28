# Static Website Hosting on Amazon S3

Hosted a static website using an Amazon S3 bucket with public access and a bucket policy — no EC2 or Amplify involved.

---

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_S3_Bucket_Objects.png
    ├── 02_S3_Bucket_Policy.png
    └── 03_Live_Website.png
```
---

## Bucket Details

| Field | Value |
|---|---|
| Bucket Name | `daynightadmin123` |
| Region | `us-east-1` |
| Block Public Access | Off |
| Hosting Type | Static website hosting |
| Endpoint | `http://daynightadmin123.s3-website-us-east-1.amazonaws.com` |

---

## What Was Done

### Step 1 — Created S3 Bucket
- Created bucket `daynightadmin123` in `us-east-1`
- Turned **Block all public access → Off**

### Step 2 — Uploaded Website Files
Uploaded 9 objects to the bucket:

| File | Type |
|---|---|
| `index.html` | HTML (entry point) |
| `login.html` | HTML |
| `projects.html` | HTML |
| `inbox.html` | HTML |
| `analytics.html` | HTML |
| `settings.html` | HTML |
| `about-templatemo.html` | HTML |
| `templatemo-daynight-script.js` | JavaScript |
| `templatemo-daynight-style.css` | CSS |

### Step 3 — Enabled Static Website Hosting
- **Properties** tab → **Static website hosting** → **Enable**
- Index document: `index.html`

### Step 4 — Applied Bucket Policy
- **Permissions** tab → **Bucket Policy** → added the following to allow public read access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::daynightadmin123/*"
    }
  ]
}
```

---

## Screenshots

### 01 — S3 Bucket Objects
*Shows all 9 uploaded files inside the `daynightadmin123` bucket.*
![S3 Bucket Objects](Screenshots/01_S3_Bucket_Objects.png)

### 02 — Bucket Policy & Public Access
*Shows Block Public Access set to Off and the applied PublicReadGetObject bucket policy.*
![S3 Bucket Policy](Screenshots/02_S3_Bucket_Policy.png)

### 03 — Live Website
*The DayNight Admin Dashboard successfully served via the S3 static website endpoint.*
![Live Website](Screenshots/03_Live_Website.png)

---

## Result

Successfully Hosted a static website using AWS s3 bucket.
