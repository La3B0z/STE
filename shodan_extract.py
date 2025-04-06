import json
import argparse

def extract_targets(json_file, output_file=None):
    targets = []

    with open(json_file, 'r') as f:
        for line_number, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
                ip = entry.get("ip_str")
                port = entry.get("port")
                if not ip or not port:
                    continue

                # Decide http or https
                scheme = "https" if port in [443, 8443] else "http"
                url = f"{scheme}://{ip}:{port}"
                targets.append(url)
            except json.JSONDecodeError as e:
                print(f"[!] Skipping line {line_number}: Invalid JSON")

    if output_file:
        with open(output_file, 'w') as out:
            for url in targets:
                out.write(url + "\n")
        print(f"[+] Extracted {len(targets)} targets to {output_file}")
    else:
        for url in targets:
            print(url)

    return targets

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract targets from Shodan JSONL")
    parser.add_argument("-i", "--input", required=True, help="Path to Shodan JSON file")
    parser.add_argument("-o", "--output", help="File to save extracted URLs")
    args = parser.parse_args()

    extract_targets(args.input, args.output)

