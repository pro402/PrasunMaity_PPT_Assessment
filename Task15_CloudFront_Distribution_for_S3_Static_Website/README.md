# CloudFront Distribution for S3 Static Website

## What Was Done
1. Uploaded 9 static files (HTML/CSS/JS — DayNight template) to S3 bucket `trials3bucketforprasun`
2. Created CloudFront distribution "Prasun website" with S3 as origin
3. Enabled OAC (Origin Access Control) — S3 bucket kept private, no public access
4. Set Viewer Protocol Policy: **Redirect HTTP to HTTPS**
5. Set Cache Policy: **CachingOptimized**; Default root object: `index.html`
6. Direct S3 URL → ❌ Blocked (403); CloudFront URL → ✅ Served via HTTPS
7. Confirmed website (DayNight dashboard) loads successfully via CloudFront URL

## Screenshots
### 01 — S3 Bucket with Website Files
*`trials3bucketforprasun` containing 9 static assets.*
![S3 Bucket](Screenshots/01_S3_Bucket_Objects.png)

### 02 — CloudFront Distribution Review Page
*Shows OAC enabled, Redirect HTTP to HTTPS, CachingOptimized policy.*
![CloudFront Config](Screenshots/02_CloudFront_Review_Create.png)

### 03 — Website Live via CloudFront
*DayNight dashboard loaded via CloudFront URL.*
![Website Live](Screenshots/03_Website_Live_CloudFront.png)
