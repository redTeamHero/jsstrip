import os
import re
import csv
import requests
from urllib.parse import urlparse

# === Config ===
INPUT_FILE = "js.txt"  # File containing list of JS URLs
OUTPUT_CSV = "js_scan_results.csv"
DOWNLOAD_DIR = "downloaded_js"
TIMEOUT = 10

# === Patterns to look for ===
patterns = {
    "API Key / Token": r"(api_key|apikey|access_token|auth_token|secret)\s*[:=]\s*[\"'][\w\-\.]+[\"']",
    "Endpoints / URLs": r"https?://[^\s\"'<>]+",
    "Dangerous Functions": r"(eval|document\.write|innerHTML|Function|setTimeout|setInterval)\s*\(",
    "Cookies / Local Storage": r"(document\.cookie|localStorage|sessionStorage)",
}

# === Setup ===
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
with open(INPUT_FILE, "r") as f:
    urls = sorted(set(line.strip() for line in f if line.strip().startswith("http")))

results = []

# === Main loop ===
for url in urls:
    print(f"[+] Fetching: {url}")
    try:
        r = requests.get(url, timeout=TIMEOUT)
        if r.status_code != 200 or 'text' not in r.headers.get("Content-Type", ""):
            continue

        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(urlparse(url).path))
        with open(filename, "w", encoding="utf-8", errors="ignore") as f:
            f.write(r.text)

        for label, regex in patterns.items():
            matches = re.findall(regex, r.text, re.IGNORECASE)
            for match in matches:
                results.append({
                    "URL": url,
                    "Type": label,
                    "Match": match
                })

    except Exception as e:
        results.append({
            "URL": url,
            "Type": "Error",
            "Match": str(e)
        })

# === Output results ===
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["URL", "Type", "Match"])
    writer.writeheader()
    writer.writerows(results)

print(f"\n✅ Scan complete. Results saved to: {OUTPUT_CSV}")
