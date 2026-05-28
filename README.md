# Offensive-Security-Tooling

## Executive Summary
This repository contains custom offensive security tools and network reconnaissance documentation. The primary focus of these builds is to understand raw network traffic, automate vulnerability enumeration, and prioritize memory-safe systems engineering.

## Network Reconnaissance (Wireshark)
* **Cleartext Protocol Interception:** Actively monitored network interfaces to capture raw TCP 3-way handshakes. Successfully intercepted and reconstructed HTTP traffic to extract unencrypted credentials, demonstrating the critical business risk of legacy cleartext protocols.
* **NAT Routing Analysis:** Mapped how internal subnet IP addresses are masked by host machines using Network Address Translation (NAT) before routing to the wider internet.

## Python Offensive Tooling
* **BleedScan (TCP Connect Scanner):** Developed a custom, lightweight Python port scanner utilizing the raw `socket` library. It is designed to automate the enumeration of external attack surfaces (like identifying open web or DNS servers) without relying on noisy, heavy frameworks.

## Rust Systems Engineering
* **Memory-Safe Target Acquisition:** Compiled a foundational command-line utility in Rust. This tool demonstrates secure parameter handling and execution. Rust was specifically chosen to prevent the memory leaks and buffer overflow vulnerabilities inherent in traditional C/C++ malware and security tooling.
