import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

CHECKPOINT_FILE = "checkpoint.json"
OUTPUT_FILE = "output.txt"

url = "https://httpbin.org/html"

# Load checkpoint
if os.path.exists(CHECKPOINT_FILE):
    with open(CHECKPOINT_FILE, "r") as f:
        checkpoint = json.load(f)
else:
    checkpoint = {"last_run": None}

print("Last run:", checkpoint["last_run"])

# Scrape
response = requests.get(url, timeout=10)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1").text.strip()
current_time = datetime.now().isoformat()

# Save output
with open(OUTPUT_FILE, "a") as f:
    f.write(f"{current_time} - {title}\n")

# Update checkpoint
checkpoint["last_run"] = current_time

with open(CHECKPOINT_FILE, "w") as f:
    json.dump(checkpoint, f, indent=2)

print("✅ Done. Checkpoint updated.")
