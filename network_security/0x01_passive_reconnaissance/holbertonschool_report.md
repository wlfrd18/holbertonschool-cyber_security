# Passive Reconnaissance Report – Holberton School

**Target Domain:** `holbertonschool.com`  
**Date:** December 2025  
**Analyst:** Wilfried Guele  

---

## 1. Objective

The objective of this report is to perform **passive reconnaissance (OSINT)** on the
`holbertonschool.com` domain using publicly available information, primarily collected
through **Shodan**.  
No active scanning or intrusive techniques were used during this assessment.

---

## 2. Hosting & Network Infrastructure

Shodan results indicate that Holberton School infrastructure is primarily hosted on
**Amazon Web Services (AWS)**.

### Cloud & Network Details

- **Cloud Provider:** Amazon Web Services (AWS)
- **Cloud Service:** EC2
- **Cloud Region:** eu-west-3 (Paris, France)
- **Organization / ISP:** Amazon Data Services France
- **ASN:** AS16509
- **Country:** France
- **City:** Paris

### Observed Public IP Addresses

The following IP addresses were observed during Shodan analysis:

| IP Address     | Hostname                                              | Subdomain                        |
|----------------|-------------------------------------------------------|----------------------------------|
| 13.37.52.4     | ec2-13-37-52-4.eu-west-3.compute.amazonaws.com         | apply.holbertonschool.com        |
| 13.39.187.93   | ec2-13-39-187-93.eu-west-3.compute.amazonaws.com       | apply.holbertonschool.com        |
| 15.236.177.62  | ec2-15-236-177-62.eu-west-3.compute.amazonaws.com      | apply.holbertonschool.com        |
| 52.47.143.83   | ec2-52-47-143-83.eu-west-3.compute.amazonaws.com       | yriry2.holbertonschool.com       |
| 52.47.114.157  | ec2-52-47-114-157.eu-west-3.compute.amazonaws.com      | read.holbertonschool.com         |

### Observed IP Ranges

Based on the identified hosts and AWS regional allocation:

- **52.47.0.0/16**
- **13.37.0.0/16**
- **15.236.0.0/16**

These ranges correspond to **AWS eu-west-3 (Paris)** infrastructure.

---

## 3. Open Ports & Services

Shodan reports the following exposed ports across the observed hosts:

| Port | Protocol | Service |
|-----:|----------|---------|
| 80   | TCP      | HTTP    |
| 443  | TCP      | HTTPS   |

These ports indicate standard web application services.

---

## 4. Identified Web Technologies

Shodan analysis reveals multiple technologies used across Holberton School subdomains.

### Web Stack

- **Web Server:** nginx 1.20.0
- **Reverse Proxy:** nginx
- **Backend Framework:** Ruby on Rails
- **Programming Language:** Ruby

### Frontend & Third-Party Services

- **JavaScript Libraries:** jQuery, Slick
- **CDN:** jsDelivr
- **Tag Management:** Google Tag Manager
- **Marketing Automation:** Klaviyo
- **Fonts & Assets:** Adobe Fonts (Typekit)

These technologies suggest a modern web application architecture with a Ruby on Rails
backend and a JavaScript-enhanced frontend.

---

## 5. TLS / SSL Configuration

TLS information collected via Shodan indicates:

- **Certificate Issuers:**
  - Amazon RSA 2048 (Amazon Trust Services)
  - Let’s Encrypt
- **Common Names (CN):**
  - apply.holbertonschool.com
  - yriry2.holbertonschool.com
- **Supported Protocols:**
  - TLS 1.2
  - TLS 1.3

No deprecated SSL or legacy TLS versions were observed.

---

## 6. Observed Subdomains

The following subdomains were identified through Shodan results and correlated data:

- holbertonschool.com
- apply.holbertonschool.com
- staging-apply.holbertonschool.com
- read.holbertonschool.com
- yriry2.holbertonschool.com

These subdomains appear to serve different purposes such as the main website,
application portal, staging environments, and internal platforms.

---

## 7. Security Observations (Passive Only)

Shodan reports potential vulnerabilities associated with the detected **nginx 1.20.0**
version. These findings are **inferred from service banners** and were **not actively
verified or exploited**.

This assessment remains strictly passive and informational.

---

## 8. Conclusion

Passive reconnaissance using Shodan shows that Holberton School infrastructure is
primarily hosted on **AWS EC2 in the eu-west-3 (Paris) region**, using a **Ruby on Rails**
application stack served behind **nginx**.  
The environment exposes standard web services (HTTP/HTTPS) with modern TLS
configurations and relies on several third-party services for analytics, content delivery,
and marketing.

This information provides a high-level overview of the organization’s public-facing
technical footprint without performing any intrusive actions.

---

*End of Report – Passive Reconnaissance (OSINT)*
