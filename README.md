# Offensive-Security-Tooling

## Executive Summary
This repository contains custom offensive security tools and network reconnaissance documentation. The primary focus of these builds is to understand raw network traffic, automate vulnerability enumeration, and prioritize memory-safe systems engineering.

## Network Reconnaissance (Wireshark)
* **Cleartext Protocol Interception:** Actively monitored network interfaces to capture raw TCP 3-way handshakes. Successfully intercepted and reconstructed HTTP traffic to extract unencrypted credentials, demonstrating the critical business risk of legacy cleartext protocols.
* **NAT Routing Analysis:** Mapped how internal subnet IP addresses are masked by host machines using Network Address Translation (NAT) before routing to the wider internet.

## Python Offensive Tooling
* **BleedScan (v1 & v2):** Developed custom, lightweight Python TCP scanners utilizing the raw `socket` library. 
  * **Version 1:** Automates the enumeration of external attack surfaces by mapping open network ports.
  * **Version 2:** Upgraded to perform active service enumeration (Banner Grabbing). Implements `try/except` error handling and uses `socket.recv()` to extract and decode service versions from open ports, transitioning the tool from mere discovery to actionable vulnerability targeting.

## Rust Systems Engineering
* **Memory-Safe Target Acquisition:** Compiled a foundational command-line utility in Rust. This tool demonstrates secure parameter handling and execution. Rust was specifically chosen to prevent the memory leaks and buffer overflow vulnerabilities inherent in traditional C/C++ malware and security tooling.
