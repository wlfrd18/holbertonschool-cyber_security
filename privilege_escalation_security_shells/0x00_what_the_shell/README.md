# What is the shell
What the Shell
Description
This project focuses on understanding how shells work and how command restrictions can be bypassed in controlled cybersecurity lab environments.

The goal is to practice shell usage, command execution, restricted shell behavior, and blacklist bypass techniques. These skills are important for both penetration testing and defensive security because they help identify weak filtering mechanisms and improve secure system design.

Learning Objectives
At the end of this project, I should be able to explain:

What a shell is and why it is important in Linux and Windows environments
How Bash and PowerShell work
How to write and execute basic shell commands
How command blacklists can be implemented
Why blacklist-based filtering is often weak
How shell features such as wildcards, escaping, and command alternatives can affect command execution
How to think creatively when working under command restrictions
Requirements
Allowed editors: vi, vim, emacs
All scripts are tested on Kali Linux
All scripts must be exactly one line long
All files must end with a new line
A README.md file is required at the root of the project directory
Project Directory
holbertonschool-cyber_security/
└── privilege_escalation_security_shells/
    └── 0x00_what_the_shell/
        ├── README.md
        └── 1-flag.txt
Task 0: Escape the Blacklist and Read the Flag
The objective of this task is to read the content of a protected file while avoiding blacklisted commands and direct file name references.

The challenge demonstrates that simple blacklist filters are not enough to securely prevent command execution or file access. Instead, stronger controls such as strict input validation, whitelisting, least privilege, and avoiding direct shell execution should be used.

Security Note
All techniques practiced in this project are intended only for a
