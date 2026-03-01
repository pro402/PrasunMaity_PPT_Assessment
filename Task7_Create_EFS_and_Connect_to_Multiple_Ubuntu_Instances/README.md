# EFS — Shared Storage Across Multiple EC2 Instances

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_EFS_Created.png
    ├── 02_Instance1_Mount_and_Write.png
    └── 03_Instance2_File_Verified.png
```

## What Was Done
1. Created EFS file system `myEFS` (`fs-0cdb4d7a11943f018`) — General Purpose, Elastic throughput, eu-north-1
2. Created Security Group with inbound **NFS TCP port 2049** and attached it to the EFS mount target (fixed timeout issue)
3. Installed `nfs-common` on both EC2 instances (`ubuntu_efs` in eu-north-1a and eu-north-1b)
4. Mounted EFS on both instances using NFS4 mount command to `~/efs-mount-point`
5. On Instance 1 (172.31.47.39): wrote `echo "Hello from 13.61.19.104" > text.txt`
6. On Instance 2 (172.31.36.166): ran `cat text.txt` → output confirmed ✅
7. Demonstrated real-time shared NFS storage across two different Availability Zones

## Screenshots
### 01 — EFS File System Created
*Shows `myEFS` in Available state with mount target changes submitted.*
![EFS Created](Screenshots/01_EFS_Created.png)

### 02 — Instance 1: Mount and Write
*Shows EFS mounted and `text.txt` written with "Hello from 13.61.19.104".*
![Instance 1 Mount and Write](Screenshots/02_Instance1_Mount_and_Write.png)

### 03 — Instance 2: File Verified
*Shows Instance 2 reading the same `text.txt` — shared storage confirmed.*
![Instance 2 File Verified](Screenshots/03_Instance2_File_Verified.png)
