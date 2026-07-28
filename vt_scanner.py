import os
import requests
import base64
from dotenv import load_dotenv

# Load key from .env file
load_dotenv()
API_KEY = os.getenv("VT_API_KEY")

def scan_url_virustotal(target_url, api_key):
    if not api_key:
        print("[!] Error: VirusTotal API Key not found. Make sure VT_API_KEY is set in your .env file.")
        return

    # Base64 encode URL for VT API v3
    url_id = base64.urlsafe_b64encode(target_url.encode()).decode().strip("=")
    api_endpoint = f"https://www.virustotal.com/api/v3/urls/{url_id}"

    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }

    print(f"[*] Querying VirusTotal for {target_url}...")
    response = requests.get(api_endpoint, headers=headers)

    if response.status_code == 200:
        data = response.json()
        stats = data['data']['attributes']['last_analysis_stats']
        malicious = stats.get('malicious', 0)
        total = sum(stats.values())

        ip_address = data['data']['attributes'].get('last_serving_ip_address', 'Not explicitly returned')

        print("\n--- Automated Investigation Results ---")
        print(f"Detections: {malicious}/{total} security vendors flagged this as malicious.")
        print(f"Resolved IP: {ip_address}")
        print("---------------------------------------")
    else:
        print(f"[!] Error making API request: HTTP {response.status_code}")

# Execution
PHISHING_URL = "https://enlineabdv--bdv-2026.replit.app/"
scan_url_virustotal(PHISHING_URL, API_KEY)
