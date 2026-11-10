# Darkweb & OSINT Rapid Triage Utility

Lightweight Python utility designed for threat intelligence desks to ingest unstructured darkweb chatter/forum dumps, strip noise, extract high-signal IOCs (IPs, cryptographic hashes, actor handles), and generate standardized Markdown incident briefs instantly.

## Features
- **IOC Extraction:** IPv4 addresses, MD5/SHA1/SHA256 hashes, threat actor handles (`@` or `u/`).
- **Standardized Output:** Executive-ready Markdown threat brief with UTC timestamping and shift recommendations.
- **Zero Dependencies:** Runs on standard Python 3.x core libraries (`re`, `datetime`, `sys`).

## Quick Start
To run the triage parser locally:

```bash
python triage_parser.py
