# VPC 3-Tier Architecture

## Project Structure
```
.
├── README.md
└── Screenshots
    ├── 01_VPC_Resource_Map.png
    ├── 02_App_Server_Private_No_Public_IP.png
    ├── 03_DB_Server_Private_No_Public_IP.png
    ├── 04_App_Server_Ping_Success.png
    └── 05_DB_Server_Ping_Fail.png
```

## What Was Done
1. Created VPC `my-3tier-vpc` (10.0.0.0/16) with 3 subnets: `web-public` (10.0.1.0/24), `app-private` (10.0.2.0/24), `db-private` (10.0.3.0/24)
2. Attached Internet Gateway `my-igw`; created NAT Gateway `my-nat-gw` (Elastic IP) in web subnet
3. Configured route tables: `public-rt` → IGW, `app-private-rt` → NAT, `db-private-rt` → local only
4. Launched 3 EC2 instances: Web-Server (public IP), App-Server (private only), DB-Server (private only)
5. SSH'd to App-Server via Web-Server bastion → `ping google.com` succeeded (outbound via NAT) ✅
6. SSH'd to DB-Server → `ping google.com` 100% packet loss (no internet route) ✅
7. Verified 3-tier isolation: Web = public, App = NAT outbound only, DB = fully isolated

## Screenshots
### 01 — VPC Resource Map
*Shows `my-3tier-vpc` with 3 subnets, IGW, NAT Gateway, and route tables.*
![VPC Resource Map](Screenshots/01_VPC_Resource_Map.png)

### 02 & 03 — App/DB Server: No Public IP
*Both private instances show no public IP warning in Connect page.*
![App Server Private](Screenshots/02_App_Server_Private_No_Public_IP.png)
![DB Server Private](Screenshots/03_DB_Server_Private_No_Public_IP.png)

### 04 — App Server: Ping Success
*`ping google.com` succeeds from `ip-10-0-2-128` via NAT.*
![App Server Ping](Screenshots/04_App_Server_Ping_Success.png)

### 05 — DB Server: Ping Fail
*`ping google.com` 100% packet loss from `ip-10-0-3-82`.*
![DB Server Ping Fail](Screenshots/05_DB_Server_Ping_Fail.png)
