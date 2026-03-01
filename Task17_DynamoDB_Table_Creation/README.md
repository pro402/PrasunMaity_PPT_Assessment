# DynamoDB Table Creation — NoSQL Database on AWS

## What Was Done
1. Created DynamoDB table `prasun-employees` — Partition key: `employee_id` (String), On-demand capacity, us-east-1
2. Inserted 4 items as JSON documents: EMP001 (Prasun Maity), EMP002 (Alex Johnson), EMP003 (Sara Smith), EMP004 (Raj Patel)
3. Each item has 5 attributes: `employee_id`, `name`, `department`, `salary`, `location` — no fixed schema required
4. Ran Scan operation via **Explore table items → Run**
5. Scan returned all 4 items — `Items returned: 4 · Items scanned: 4 · Efficiency: 100%` ✅
6. Table ARN: `arn:aws:dynamodb:us-east-1:198116961487:table/prasun-employees`

## Screenshots
### 01 — DynamoDB Table Active
*Shows `prasun-employees` with partition key `employee_id (String)`, On-demand capacity, Table status Active.*
![DynamoDB Table](Screenshots/01_DynamoDB_Table_Active.png)

### 02 — Scan Result — All Items
*Explore items page showing all 4 records returned from Scan with 100% efficiency.*
![DynamoDB Scan](Screenshots/02_DynamoDB_Scan_Items.png)
