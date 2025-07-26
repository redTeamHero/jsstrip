📄 Description

jsstrip.py is a reconnaissance and static analysis tool designed for red teamers, bug bounty hunters, and security researchers. It automates the process of fetching, scanning, and analyzing remote JavaScript files to uncover potential security risks and exposed information.
🎯 Purpose

This tool helps identify:

    ✅ Leaked API keys or tokens

    ✅ Hardcoded third-party endpoints

    ✅ Dangerous client-side JavaScript functions

    ✅ Access to cookies and local/session storage

By scanning JavaScript URLs, it highlights potential attack surfaces in web applications — such as development/debug logic, hardcoded secrets, or insecure client-side practices.
🧰 Features

    📥 Bulk Fetching – Reads a list of URLs from js.txt and downloads each .js file.

    🔎 Regex-based Static Analysis – Scans each file for:

        API keys, tokens, secrets

        External URLs (API endpoints, tracking services)

        JavaScript functions like eval, innerHTML, document.write

        Local/session storage and cookie access

    📂 File Output – Saves downloaded scripts to downloaded_js/ for manual inspection.

    📊 Report Generation – Outputs scan results to a CSV file (js_scan_results.csv) for easy filtering or import into other tools.

⚙️ Configuration
Parameter	Value	Description
INPUT_FILE	js.txt	Text file with one JS URL per line
OUTPUT_CSV	js_scan_results.csv	Output CSV report with matches and errors
DOWNLOAD_DIR	downloaded_js/	Folder where JS files are saved
TIMEOUT	10	
