# Disk Partitioning — MBR (Ubuntu) & GPT (Windows Server)

This task demonstrates how to create and manage disk partitions using two partitioning schemes: **MBR (Master Boot Record)** on Ubuntu Linux using `fdisk`, and **GPT (GUID Partition Table)** on Windows Server using **Server Manager**.

---

## Project Structure
```
.
├── Commands.txt
├── README.md
└── Screenshots
    ├── MBR_Ubuntu_fdisk_helper.png 
    ├── MBR_Ubuntu_fdisk.png
    └── GPT_Windows_ServerManager.png
```
---

## Key Concepts

| Feature | MBR | GPT |
|---|---|---|
| Full Form | Master Boot Record | GUID Partition Table |
| Max Disk Size | 2 TB | 9.4 ZB |
| Max Partitions | 4 primary | 128 primary |
| OS Support | Linux, older Windows | Modern Windows, Linux, macOS |
| Boot Support | BIOS | UEFI |

---

## Part 1: MBR Partitioning on Ubuntu (fdisk)

### Prerequisites
- A secondary unpartitioned disk attached to your Ubuntu machine.
- Root or sudo access.

### Commands Used

**1. List all block devices to identify the target disk**
```bash
lsblk
```

**2. View full disk details**
```bash
sudo fdisk -l
```

**3. Open the target disk with fdisk**
```bash
sudo fdisk /dev/nvme1n1
```
Inside the `fdisk` interactive prompt:

| Command | Action |
|---|---|
| `n` | Create a new partition |
| `p` | Select primary partition type |
| `1` | Set partition number to 1 |
| Enter | Accept default first sector |
| Enter | Accept default last sector (full disk) |
| `w` | Write changes and exit |

**4. Verify the new partition**
```bash
sudo fdisk -l /dev/nvme1n1
lsblk
```

**5. Format the partition with ext4**
```bash
sudo mkfs.ext4 /dev/nvme1n1p1
```

**6. Mount the partition and verify**
```bash
sudo mkdir /mnt/mypartition
sudo mount /dev/nvme1n1p1 /mnt/mypartition
df -h
```

---

## Part 2: GPT Partitioning on Windows Server (Server Manager)

### Prerequisites
- A secondary unallocated disk attached to your Windows Server instance.
- Administrator access.

### Steps

**1. Open Server Manager**
- Launch **Server Manager** from the Start menu or taskbar.

**2. Navigate to Disks**
- Go to **File and Storage Services** → **Volumes** → **Disks**.

**3. Initialize the Disk**
- Right-click the uninitialized disk → **Initialize**.
- Confirm the prompt — Windows will initialize it using **GPT** by default on modern systems.

**4. Create a New Volume**
- Right-click the initialized disk → **New Volume**.
- Follow the New Volume Wizard:
  - Select the disk → Set volume size.
  - Assign a drive letter (e.g., `E:`).
  - Choose file system: **NTFS**.
  - Set a volume label → Click **Create**.

**5. Verify**
- The volume appears as **Online** under File and Storage Services.
- Confirm the drive is accessible via **File Explorer**.

---

## Screenshots

### MBR Partitioning — Ubuntu (fdisk)
*Shows lsblk output, fdisk partition creation on /dev/nvme1n1, and df -h confirming the mounted partition.*
![MBR Ubuntu fdisk](Screenshots/MBR_Ubuntu_fdisk.png)

### GPT Partitioning — Windows Server (Server Manager)
*Shows the initialized GPT disk and the new NTFS volume created via Server Manager → File and Storage Services.*
![GPT Windows Server Manager](Screenshots/GPT_Windows_ServerManager.png)

---

## Observations

- The disk `/dev/nvme1n1` is an NVMe (Non-Volatile Memory Express) SSD, commonly attached on AWS EC2 instances.
- MBR is limited to **4 primary partitions** and a maximum disk size of **2 TB**.
- GPT supports up to **128 primary partitions** and is the preferred scheme for modern UEFI-based systems.
- Server Manager's **File and Storage Services** is the recommended GUI method for disk management on Windows Server environments.
- Always verify the target disk using `lsblk` or `fdisk -l` before partitioning to avoid accidental data loss.
