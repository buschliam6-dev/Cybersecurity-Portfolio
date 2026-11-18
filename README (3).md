Project 3: Basic Pentesting 1 – Case Study

Overview

This project involved conducting a basic penetration test against an Ubuntu virtual machine in a controlled lab environment. The objective was to identify active network devices, discover running services, research vulnerabilities, perform controlled exploitation, and demonstrate the importance of password security.

Tools Used

- Kali Linux
- Nmap
- ARP Scan
- Metasploit Framework
- John the Ripper
- Ubuntu Virtual Machine

Assessment Stages

Stage 1: Network Scanning and Service Identification

I used ARP scanning to identify active devices on the local network and Nmap to scan the target machine.

Target IP: "192.168.57.3"

The scan identified the following open ports:

Port| Service| Version
21| FTP| ProFTPD 1.3.3c
22| SSH| OpenSSH 7.2p2
80| HTTP| Apache 2.4.18

The results confirmed that the target machine was running three accessible services.

Stage 2: Vulnerability Research

I researched the identified service versions to determine whether known vulnerabilities existed.

The main finding was a backdoor vulnerability affecting ProFTPD 1.3.3c.

The vulnerability is identified as CVE-2010-2013 and was associated with a compromised ProFTPD source archive.

This vulnerability could allow unauthenticated remote command execution under vulnerable conditions.

Stage 3: Exploitation Using Metasploit

I used the Metasploit Framework to test the identified ProFTPD vulnerability in the controlled lab environment.

Module used:
"exploit/unix/ftp/proftpd_133c_backdoor"

Target IP: "192.168.57.3"

Payload: "cmd/unix/bind_perl"

Listening port: "4444"

After running the exploit, Metasploit successfully established a command shell.

I verified the access level using the "whoami" command, which returned "root".

This confirmed successful root-level access to the target machine.

Stage 4: Password Extraction and Password Cracking

After obtaining root access, I accessed the Linux password hash information stored in:

"/etc/shadow"

I identified the relevant password hash and saved it into a file named:

"Hashes.txt"

I then used John the Ripper to attempt to recover the original password.

The cracking process successfully recovered one password hash.

This demonstrated the security risks associated with weak passwords and the importance of strong password policies.

Login Verification

I used the recovered credentials to perform a final login verification on the Ubuntu virtual machine.

Successful access to the Ubuntu desktop confirmed that the recovered credentials worked.

Key Findings

- Identified active devices on a local network.
- Discovered open ports and running services using Nmap.
- Identified a known ProFTPD 1.3.3c backdoor vulnerability.
- Successfully demonstrated exploitation using Metasploit.
- Obtained and verified root-level access in the lab.
- Extracted password hash information and demonstrated password cracking with John the Ripper.
- Verified access through the Ubuntu desktop.

Security Recommendations

- Update vulnerable software and services.
- Disable unnecessary network services and open ports.
- Secure FTP services or replace unencrypted FTP with SFTP.
- Use strong, unique passwords.
- Restrict access to sensitive system files such as "/etc/shadow".
- Monitor systems for suspicious activity.
- Regularly perform vulnerability assessments.

Conclusion

This assessment provided practical experience in network reconnaissance, service identification, vulnerability research, exploitation, and password security testing.

It demonstrated how an outdated and vulnerable service can expose a system to serious security risks.

The project strengthened my understanding of penetration testing methodologies and the importance of identifying and addressing security vulnerabilities.

Environment: Controlled Ubuntu virtual machine lab.

Assessment Date: 3 November 2026.