# CloudWatch Alarm — 70% CPU Auto Stop + Email Alert

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_CloudWatch_Alarm_Created.png
    ├── 02_stress_ng_running.png
    ├── 03_CPU_Graph_Spike.png
    ├── 04_EC2_Auto_Stopped.png
    └── 05_Email_Alert_Received.png
```

## What Was Done
1. Launched EC2 instance `StressInstance` (t3.micro, `i-034ad9362c3574f27`)
2. Created CloudWatch alarm `high-cpu-stop-ec2`: CPUUtilization > 70%, 1-min period
3. Added two alarm actions: **Stop EC2 instance** + **publish to SNS `website-down-alerts`**
4. Ran `stress-ng --cpu 0 --timeout 300s` to spike CPU on EC2
5. CPU reached 76.1% — CloudWatch alarm transitioned to ALARM state within 1 minute
6. EC2 instance **automatically stopped** — zero manual intervention ✅
7. SNS email received: `ALARM: "high-cpu-stop-ec2" in US East (N. Virginia)` ✅

## Screenshots
### 01 — CPU Graph Spike
*Shows `high-cpu-stop-ec2` alarm with CPU crossing the 70% threshold.*
![Alarm Graph](Screenshots/03_CPU_Graph_Spike.png)

### 02 — stress-ng Terminal Output
*Shows `stress-ng --cpu 0 --timeout 300s` running with 2 CPU workers.*
![stress-ng](Screenshots/02_stress_ng_running.png)

### 03 — EC2 Instance Auto Stopped
*Shows `StressInstance` in Stopped state — triggered by CloudWatch alarm action.*
![EC2 Stopped](Screenshots/04_EC2_Auto_Stopped.png)

### 04 — Email Alert
*Shows AWS email confirming CPU crossed 76.1% at 19:40:12 UTC.*
![Email](Screenshots/05_Email_Alert_Received.png)
