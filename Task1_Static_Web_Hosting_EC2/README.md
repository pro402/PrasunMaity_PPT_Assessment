# Static Website Hosting on AWS EC2 with Nginx

This project demonstrates how to deploy and host a static website on an Amazon Web Services (AWS) EC2 instance. It utilizes an Nginx web server to serve a GlassAdmin Dashboard template (provided by TemplateMo) on an Ubuntu machine.

## Project Structure

```text
.
├── Commands.txt
├── README.md
└── Screenshots
    ├── EC2_setup.png
    └── Hosted_Static_Website.png
```
## Prerequisites

- An active AWS Account.
- An EC2 instance running Ubuntu (e.g., Ubuntu 24.04 LTS).
- Security Group configured to allow **SSH (Port 22)** and **HTTP (Port 80)** inbound traffic.
- SSH access to your EC2 instance.

## Deployment Steps

Follow these steps to configure the server and deploy the website. All terminal commands are also available in `Commands.txt`.

**1. Update the Package List**

Ensure your server's package index is up-to-date:

    sudo apt update

**2. Install Nginx and Unzip Utilities**

Install the Nginx web server and the tools required to extract the downloaded template:

    sudo apt install nginx -y
    sudo apt install zip unzip -y

**3. Download the Website Template**

Fetch the static website template directly to your EC2 instance using `wget`:

    wget -O webpage.zip https://templatemo.com/download/templatemo_607_glass_admin

**4. Extract and Deploy**

Unzip the downloaded archive and copy its contents into the default Nginx web directory (`/var/www/html/`):

    unzip webpage.zip
    sudo cp -r templatemo_607_glass_admin/. /var/www/html/

**5. Verify the Deployment**

Navigate to your EC2 instance's Public IPv4 address in any web browser to view the live website:

    http://<your-ec2-public-ip>

## Screenshots

### AWS EC2 Instance Setup
*Displays the running Ubuntu t3.micro instance and its networking details.*
![EC2 Setup](Screenshots/EC2_setup.png)

### Live Hosted Website
*The deployed GlassAdmin Dashboard served successfully via Nginx over HTTP.*
![Hosted Static Website](Screenshots/Hosted_Static_Website.png)