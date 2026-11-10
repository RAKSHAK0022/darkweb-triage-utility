#!/usr/bin/env python3
import re
import sys
from datetime import datetime

def parse_intelligence_feed(raw_text):
    # Regex patterns for high-signal IOCs and actor markers
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    md5_sha_pattern = r'\b([a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64})\b'
    handle_pattern = r'(?:@|u\/)([a-zA-Z0-9_-]+)'

    ips = list(set(re.findall(ip_pattern, raw_text)))
    hashes = list(set(re.findall(md5_sha_pattern, raw_text)))
    handles = list(set(re.findall(handle_pattern, raw_text)))

    brief = f"""
# THREAT INTEL RAPID TRIAGE BRIEF
**Generated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC
**Classification:** Operational Recon / Deep & Darkweb Desk

## 1. Extracted Indicators of Compromise (IOCs)
- **IP Addresses:** {ips if ips else "None detected in raw payload"}
- **Cryptographic Hashes:** {hashes if hashes else "None detected in raw payload"}
- **Identified Threat Actors / Handles:** {handles if handles else "None detected"}

## 2. Recommended Shift Action
1. Cross-reference extracted IP/Hashes against active SIEM telemetry and commercial feeds.
2. If actor handles match known state-sponsored or cybercrime syndicates, escalate to lead analyst for TTP mapping.
3. Archive raw payload into historical repository for trend analysis.
"""
    return brief

if __name__ == "__main__":
    # Sample raw text simulation from an unstructured dark web forum scrape
    sample_payload = """
    Target acquisition confirmed on target network. Initial access via compromised endpoint 192.168.10.45.
    Deploying payload variant hash a591a6d40bf420404a011733cfb7b190d62c65bf0bc982b6c25785afbc0fc511.
    Collaborated with operator u/DarkShadow99 on the forum.
    """
    print(parse_intelligence_feed(sample_payload))