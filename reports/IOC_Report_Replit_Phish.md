# Incident Report: Phishing Landing Page Triage

## 1. Executive Summary
An active phishing campaign targeting Banco de Venezuela (BDV) credentials was analyzed via PhishTank data. The attacker leveraged Replit cloud hosting to deploy a fake login portal to bypass standard web reputation checks.

## 2. Attack Chain Mapping
[Phishing Link / Email] ➔ [Malicious URL: https://enlineabdv--bdv-2026.replit.app/] ➔ [IP: 34.117.33.233] ➔ [Credential Harvesting Page]

## 3. Indicators of Compromise (IOCs)
- **Domain:** `enlineabdv--bdv-2026.replit.app`
- **URL:** `https://enlineabdv--bdv-2026.replit.app/`
- **IP Address:** `34.117.33.233` (Google Cloud / Replit)
- **Detection Score:** 16/92 Security Vendors (VirusTotal)

## 4. Technical Analysis
- **Domain Spoofing:** The subdomain name contains `enlineabdv` mimicking Banco de Venezuela's online banking service.
- **Hosting Strategy:** The threat actor is using Replit (`replit.app`) to acquire a free, valid SSL/TLS certificate and trusted domain reputation.

## 5. Mitigation & Recommendations
1. **Block Rule:** Add `enlineabdv--bdv-2026.replit.app` to perimeter web proxy blocklists.
2. **Abuse Reporting:** Submit an abuse ticket to Replit (`abuse@replit.com`) to take down the hosted instance.
3. **Detection Rule:** Search DNS logs for internal endpoints requesting resolution for `*.replit.app` subdomains containing `bdv` or banking terms.
