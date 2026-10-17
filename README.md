# Cybersecurity Master Portfolio & Learning Repository

> **Autonomous Security Engineering, Practical Cyber Defense & Penetration Testing**  
> *Follows the Cybersecurity Master Roadmap Architecture (Tier 0 to Tier 5)*

---

## 🎯 Repository Purpose
This repository serves as a verifiable, public proof-of-work portfolio documenting hands-on labs, custom security tooling, network packet dissections, Active Directory penetration tests, and defensive engineering artifacts.

---

## 🗂️ Directory Architecture

```text
Cybersecurity/
├── Foundations/              # Computer Architecture, Operating System Internals
│   ├── Computer-Architecture/
│   └── Operating-Systems/
├── Networking/               # Packet Analysis, Protocol RFCs, Subnetting
│   ├── Subnetting-Notes/
│   ├── Protocol-Dissections/
│   └── PCAP-Analyses/
├── Linux/                    # Administration, CIS Hardening, Auditd
│   ├── Admin-Scripts/
│   ├── Hardening-Playbooks/
│   └── Auditd-Rules/
├── Windows/                  # Enterprise Administration, Sysmon, PowerShell
│   ├── PowerShell-Automation/
│   ├── Sysmon-Configs/
│   └── Incident-Collector/
├── Python-Security/          # Custom Scanners, Network Sockets, Automation
│   ├── Recon-Suite/
│   └── Custom-Scanners/
├── Web-Security/             # PortSwigger Labs, OWASP Top 10, Exploits
│   ├── PortSwigger-Labs/
│   ├── Exploit-PoCs/
│   └── Audit-Reports/
├── SOC/                      # SIEM Alerts, Splunk SPL, Triage Playbooks
│   ├── SIEM-Dashboards/
│   ├── Splunk-SPL-Queries/
│   └── Triage-Playbooks/
├── DFIR/                     # Digital Forensics, Memory Analysis, Volatility
│   ├── Memory-Analyses/
│   ├── Disk-Timelines/
│   └── Ransomware-Reports/
├── Active-Directory/         # Kerberos, BloodHound Paths, GPO Hardening
│   ├── Lab-Automation/
│   ├── BloodHound-Analyses/
│   └── Hardening-GPOs/
├── Security-Engineering/     # Production REST APIs, Hardened Services
│   └── Vuln-Sentinel-API/
├── Cloud/                    # AWS & Azure Security, Terraform Blueprints
│   ├── AWS-Terraform-Blueprints/
│   └── CSPM-Audit-Reports/
├── Kubernetes/               # Container Hardening, Falco Runtime Rules
│   ├── Hardened-Cluster-Config/
│   └── Falco-Rules/
├── DevSecOps/                # CI/CD Security, SAST, SBOM, Dependency Scans
│   └── CI-CD-Security-Pipelines/
├── AI-Security/              # LLM Red Teaming, Guardrails, RAG Defense
│   ├── RAG-CVE-Engine/
│   └── LLM-Guardrail-Redteam/
├── Threat-Intel/             # Diamond Model, APT Dossiers, YARA Rules
│   ├── APT-Dossiers/
│   └── Custom-YARA-Rules/
├── Detection-Engineering/    # Detection-as-Code, SigmaHQ Rules
│   └── SigmaHQ-Detection-as-Code/
├── Exploit-Development/      # Binary Exploitation, ROP Chains, Shellcode
│   ├── ROP-Chains/
│   └── Custom-Shellcode/
├── Malware-Analysis/         # Static & Dynamic Triage, Flare-VM Analysis
│   └── Triage-Reports/
├── Frontier-Specialization/  # IoT Firmware, SCADA/ICS Modbus, PQC
│   ├── IoT-Firmware-Audits/
│   ├── ICS-Modbus-Monitors/
│   └── PQC-Benchmarking/
├── CTF-Writeups/             # Structured Walkthroughs
│   ├── HackTheBox/
│   └── TryHackMe/
└── Research/                 # Technical Whitepapers & Case Studies
    └── Whitepapers/
```

---

## ⚡ Git Hygiene & Commit Conventions
- **Feat**: New custom tool, scanner, or complete lab topology (`feat: implement multi-threaded SYN port scanner in python`)
- **Docs**: Lab writeup, architecture diagram, or report (`docs: complete Wireshark TCP handshake analysis report`)
- **Fix**: Remediated configuration, patched exploit script (`fix: patch LFI vulnerability in test web server`)
- **Sec**: Defensive hardening, Sigma rule, firewall rule (`sec: deploy auditd rule to monitor /etc/shadow modifications`)

---

## ⚖️ Authorized Testing & Legal Boundaries
All security assessments, exploit scripts, and network traffic analyses documented within this repository are conducted strictly inside authorized virtual laboratories, CTF platforms, or systems under explicitly signed Rules of Engagement (RoE). Unsanctioned exploitation against unauthorized public systems is strictly illegal under the Bharatiya Nyaya Sanhita (BNS) 2023, Information Technology Act 2000, and international cybersecurity laws.
