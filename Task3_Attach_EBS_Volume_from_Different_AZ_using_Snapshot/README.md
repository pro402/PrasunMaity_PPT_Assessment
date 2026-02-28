# EBS Disk Partitioning & Cross-AZ Migration

Partitioned an EBS volume on an EC2 instance in **us-east-1a**, wrote a file, then migrated the data to **us-east-1b** via snapshot and verified the file was intact.

---

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_EC2_1a_Volume_Attached.png
    ├── 02_Attach_Volume_1b_Console.png
    └── 03_Terminal_1b_File_Verified.png
```
---

## What Was Done

### Step 1 — Partition & Write (us-east-1a)

```bash
sudo lsblk
sudo fdisk /dev/nvme1n1          # created partition nvme1n1p1
sudo mkfs.ext4 /dev/nvme1n1p1
sudo mkdir /mnt/mypartition
sudo mount /dev/nvme1n1p1 /mnt/mypartition
sudo nano /mnt/mypartition/text.txt
# Content: "Hello i am in AZ us-east-1a"
```

### Step 2 — Snapshot (AWS Console)

- Selected the 10 GiB volume → **Actions → Create Snapshot**
- Waited for status: `pending` → `completed`

### Step 3 — New Volume in us-east-1b (AWS Console)

- Snapshot → **Create Volume from Snapshot** → AZ set to `us-east-1b`
- Attached the new volume to instance `Ubuntu_AZ_US_1b` at `/dev/sdd`

### Step 4 — Mount & Verify (us-east-1b)

```bash
lsblk
sudo mkdir /mnt/mypartition
sudo mount /dev/nvme1n1p1 /mnt/mypartition
cd /mnt/mypartition/
ls                 # lost+found  text.txt
cat text.txt       # Hello i am in AZ us-east-1a ✓
```

---

## Screenshots

### EC2 Instance (us-east-1a) — Volume Attached
![EC2 1a Volume Attached](Screenshots/01_EC2_1a_Volume_Attached.png)

### Attaching Snapshot Volume to us-east-1b
![Attach Volume Console](Screenshots/02_Attach_Volume_1b_Console.png)

### File Verified on us-east-1b
![Terminal Verification](Screenshots/03_Terminal_1b_File_Verified.png)

---

## Result

`text.txt` written in `us-east-1a` was successfully read in `us-east-1b`, confirming data persistence across Availability Zones via EBS snapshot.

