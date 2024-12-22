from xpath_util import get_opponents, get_fighter_info
import requests
import json
import sys

if len(sys.argv) == 1:
    raise Exception("Missing argument(s)...")

target = sys.argv[1]
url = sys.argv[2]
output_name = sys.argv[3]

handler = None
if target == "ops":
    handler = get_opponents
elif target == "info":
    handler = get_fighter_info

response = requests.get(url)
print(response.status_code)

results = handler(response.text)
jsonContent = json.dumps(results)

with open(output_name, "w", encoding="utf-8") as f:
    f.write(jsonContent)
