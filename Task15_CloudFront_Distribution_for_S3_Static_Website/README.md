# CloudFront Distribution for S3 Static Website

Deployed a static website on Amazon S3 and configured a CloudFront CDN distribution to serve it globally with HTTPS, edge caching, and low latency.

---

## Architecture

```
Browser → CloudFront Edge Location (HTTPS)
              ↓
    S3 Origin (trials3bucketforprasun)
              ↓
    Static Website Files (index.html, CSS, JS)
```

---

## Resources

| Resource | Name / Value |
|---|---|
| S3 Bucket | `trials3bucketforprasun` |
| S3 Region | `us-east-1` (N. Virginia) |
| Distribution Name | `Prasun website` |
| S3 Origin | `trials3bucketforprasun.s3.us-east-1.amazonaws.com` |
| Origin Access | CloudFront managed (OAC) |
| WAF | Disabled |
| Billing | Pay-as-you-go ($0/month) |

---

## S3 Bucket Contents

| File | Type | Size |
|---|---|---|
| `index.html` | HTML | 38.4 KB |
| `about-templatemo.html` | HTML | 18.9 KB |
| `analytics.html` | HTML | 22.7 KB |
| `inbox.html` | HTML | 16.8 KB |
| `login.html` | HTML | 6.8 KB |
| `projects.html` | HTML | 16.0 KB |
| `settings.html` | HTML | 17.8 KB |
| `templatemo-daynight-script.js` | JS | 8.4 KB |
| `templatemo-daynight-style.css` | CSS | 33.7 KB |

---

## CloudFront Distribution Configuration

| Setting | Value |
|---|---|
| Origin Domain | `trials3bucketforprasun.s3.us-east-1.amazonaws.com` |
| Origin Path | `/` (root) |
| Grant CloudFront Access to Origin | Yes (OAC) |
| Enable Origin Shield | No |
| Connection Attempts | 3 |
| Connection Timeout | 10 seconds |
| Viewer Protocol Policy | **Redirect HTTP to HTTPS** |
| Allowed HTTP Methods | GET, HEAD |
| Cache Policy | **CachingOptimized** |
| Default Root Object | `index.html` |
| Security Protections (WAF) | None |

---

## What is OAC (Origin Access Control)?

Since **Grant CloudFront access to origin = Yes** was selected, CloudFront automatically updates the S3 bucket policy to **restrict direct S3 access**. Only requests routed through CloudFront are served — the S3 bucket itself is not publicly accessible. This is the recommended security model.

```
Direct S3 URL  → ❌ Blocked (403 Access Denied)
CloudFront URL → ✅ Served via HTTPS
```

---

## Screenshots

### 01 — S3 Bucket with Website Files
*`trials3bucketforprasun` containing 9 static assets — HTML pages, JS, and CSS for the DayNight template.*

![S3 Bucket](Screenshots/01_S3_Bucket_Objects.png)

### 02 — CloudFront Distribution Review Page
*Shows distribution named "Prasun website" with S3 origin, OAC enabled, Redirect HTTP to HTTPS, and CachingOptimized policy before final creation.*

![CloudFront Config](Screenshots/02_CloudFront_Review_Create.png)

### 03 — Website Live via CloudFront
*DayNight dashboard loaded successfully via the CloudFront distribution URL, confirming CDN delivery is working.*

![Website Live](Screenshots/03_Website_Live_CloudFront.png)

---

## Key Concepts

**Why CloudFront over direct S3?**

| Feature | S3 Direct | CloudFront |
|---|---|---|
| Protocol | HTTP only | HTTPS enforced |
| Latency | Single region | 400+ edge locations globally |
| Caching | None | Edge cache (CachingOptimized) |
| Security | Public bucket needed | OAC — bucket stays private |
| Cost at scale | Higher egress | Lower (cached responses) |

---

## Result

The static website (DayNight template) was successfully deployed on S3 and distributed globally via CloudFront. Requests are automatically upgraded to HTTPS, content is cached at edge locations, and the S3 bucket is kept private through Origin Access Control — demonstrating production-grade CDN setup on AWS.

