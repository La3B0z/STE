This Python script parses Shodan JSONL export files and extracts IP addresses and ports into usable HTTP/HTTPS URLs for scanning or testing.

📂 Input Format
Supports Shodan JSONL files (one JSON object per line), such as from:

shodan download --limit 1000 tomcat.json.gz apache:tomcat
gunzip tomcat.json.gz

📌 Example Input (tomcat.json)

{"ip_str": "196.217.155.227", "port": 8009, "transport": "tcp"}
{"ip_str": "203.0.113.10", "port": 443}
{"ip_str": "10.0.0.5", "port": 8080}

🛠 Usage

python3 shodan_extract.py -i tomcat.json -o targets.txt

* -i / --input: Path to your Shodan JSONL file
* -o / --output: File to save extracted URLs (optional)

📤 Output Format
Each line will look like:
http://196.217.155.227:8009
https://203.0.113.10:443
http://10.0.0.5:8080

✅ Features
- Handles multi-line JSONL format (Shodan default)
- Automatically chooses http:// or https:// based on port
- Ignores invalid or incomplete lines
- Gives clean, ready-to-use target lists for automation tools

🔒 Disclaimer
This tool is intended only for ethical hacking, research, or authorized security testing.
Do not scan or interact with systems you do not have permission to test.
