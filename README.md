 # Create the README.md file with repo documentation
echo "# Darkweb & OSINT Rapid Triage Utility

Lightweight Python utility designed for threat intelligence desks to ingest unstructured darkweb chatter/forum dumps, strip noise, extract high-signal IOCs (IPs, cryptographic hashes, actor handles), and generate standardized Markdown incident briefs instantly.

## Features
- Extracted IOC Types: IPv4 addresses, MD5/SHA1/SHA256 hashes, threat actor handles (@/u/).
- Output Format: Executive-ready Markdown threat brief with UTC timestamping and shift recommendations.
- Zero Dependencies: Runs on standard Python 3.x libraries (\`re\`, \`datetime\`, \`sys\`).

## Quick Start
\`\`\`bash
python triage_parser.py
\`\`\`
" > README.md

# Stage, commit, and push the README
git add README.md
git commit -m "docs: add README documentation"
git push
