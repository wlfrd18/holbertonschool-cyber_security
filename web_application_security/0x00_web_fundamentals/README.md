# 0x00 - Web Fundamentals

## Description

This project is an introduction to **Web Application Security**.  
It focuses on understanding how web applications work and how common
vulnerabilities can be identified and exploited using standard security tools.

Throughout this module, we interact with a target web application and perform
basic reconnaissance and exploitation using command-line tools such as `curl`
and `sqlmap`.

---

## Environment

All tasks were completed using the following environment:

- **Operating System**: Kali GNU/Linux Rolling  
- **Kali Version**: 2025.2  
- **Architecture**: x86_64  

---

## Tools Used

### curl
- **Version**: 8.18.0-rc3  
- **Purpose**:  
  - Sending HTTP requests
  - Testing endpoints
  - Verifying connectivity to the target web application

### sqlmap
- **Version**: 1.9.12#stable  
- **Purpose**:  
  - Automated SQL injection detection
  - Database enumeration and exploitation

---

## Target Setup

- **Target URL**: `http://web0x00.hbtn`
- The domain `web0x00.hbtn` is mapped locally to the target machine IP
  by editing the `/etc/hosts` file.

Example:
```bash
sudo bash -c "echo '<TARGET_IP> web0x00.hbtn' >> /etc/hosts"
