# RDS MySQL Database + DBeaver Connection & SQL Queries

Launched an Amazon RDS MySQL instance, connected to it using DBeaver, created a table, inserted records, and executed SELECT, filter, and aggregate queries.

---

## Architecture

```
DBeaver (Local Machine) → Port 3306 → Security Group → RDS MySQL (us-east-1)
```

---

## Resources

| Resource | Value |
|---|---|
| RDS Instance | `prasun-rds-db` |
| Engine | MySQL 8.0 |
| Instance Class | db.t3.micro (Free Tier) |
| Region | us-east-1b |
| Endpoint | `prasun-rds-db.cg9eqmomuu7n.us-east-1.rds.amazonaws.com` |
| Port | 3306 |
| Master Username | `admin` |
| VPC | `vpc-0bb6e69e1e9c555ec` (Default) |
| Security Group | `default (sg-0e88c8479dc3336bd)` |
| Client Tool | DBeaver 25.3.5 |

---

## Setup Steps

### 1 — Launch RDS Instance
- Engine: MySQL 8.0, Template: Free Tier
- Public access: **Yes**, Security group inbound: port `3306` open
- Initial DB: `mysql`

### 2 — Connect via DBeaver
- New Connection → MySQL
- Host: `prasun-rds-db.cg9eqmomuu7n.us-east-1.rds.amazonaws.com`
- Port: `3306`, Username: `admin`
- Driver property: `allowPublicKeyRetrieval = true`, `useSSL = false`
- Test Connection → ✅ Connected

---

## Database & Table

```sql
CREATE DATABASE prasundb;
```

```sql
CREATE TABLE employees (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    department  VARCHAR(50),
    salary      DECIMAL(10,2),
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## Data Inserted

```sql
INSERT INTO employees (name, department, salary) VALUES
('Prasun Maity', 'Cloud Engineering',   85000.00),
('Alex Johnson', 'DevOps',              78000.00),
('Sara Smith',   'Backend Development', 92000.00),
('Raj Patel',    'Data Engineering',    88000.00);
```

---

## Query Outputs

### Query 1 — SELECT * (All Records)
```sql
SELECT * FROM employees;
```
| id | name | department | salary | created_at |
|---|---|---|---|---|
| 1 | Prasun Maity | Cloud Engineering | 85,000 | 2026-02-28 20:23:48 |
| 2 | Alex Johnson | DevOps | 78,000 | 2026-02-28 20:23:48 |
| 3 | Sara Smith | Backend Development | 92,000 | 2026-02-28 20:23:48 |
| 4 | Raj Patel | Data Engineering | 88,000 | 2026-02-28 20:23:48 |

### Query 2 — Filter (salary > 80,000)
```sql
SELECT name, salary FROM employees WHERE salary > 80000;
```
| name | salary |
|---|---|
| Prasun Maity | 85,000 |
| Sara Smith | 92,000 |
| Raj Patel | 88,000 |

### Query 3 — Aggregate (AVG salary by department)
```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;
```
| department | avg_salary |
|---|---|
| Cloud Engineering | 85,000 |
| DevOps | 78,000 |
| Backend Development | 92,000 |
| Data Engineering | 88,000 |

---

## Screenshots

### 01 — RDS Connectivity & Security
*Shows `prasun-rds-db` endpoint, port 3306, and security group details in the AWS console.*

![RDS Console](Screenshots/01_RDS_Endpoint_Console.png)

### 02 — SELECT * Query Output
*DBeaver showing all 4 employee records returned from `SELECT * FROM employees`.*

![Select All](Screenshots/02_DBeaver_Select_All.png)

### 03 — Filter Query Output
*DBeaver showing 3 employees with salary > 80,000 from the WHERE clause query.*

![Filter Query](Screenshots/03_DBeaver_Filter_Query.png)

### 04 — Aggregate Query Output
*DBeaver showing AVG salary grouped by department using GROUP BY.*

![Aggregate Query](Screenshots/04_DBeaver_Aggregate_Query.png)

---

## Key Concepts

| Concept | Explanation |
|---|---|
| RDS | AWS fully managed relational DB — no OS/DB patching needed |
| Multi-AZ | High availability via automatic failover (not used here — free tier) |
| Security Group | Acts as a firewall — port 3306 must be open for external access |
| Public Access | Must be enabled for connecting from outside the VPC |
| OAC (allowPublicKeyRetrieval) | Required for MySQL 8.0 `caching_sha2_password` auth plugin |

---

## Result

Successfully launched an RDS MySQL instance, connected via DBeaver from a local Ubuntu machine, created the `employees` table, inserted 4 records, and executed SELECT, WHERE filter, and GROUP BY aggregate queries — demonstrating end-to-end managed database usage on AWS.

