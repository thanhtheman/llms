import requests
import json

# API endpoint
url = "https://housesigma.com/bkv2/api/search/homepage/recommendlist_v2"

# Headers
headers = {
    "Authorization": "Bearer 20231005r3ro2udthtri6sgi4dla0sc3uv",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Dnt": "1",
    "Origin": "https://housesigma.com",
    "Pragma": "no-cache",
    "Referer": "https://housesigma.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    # Add any other headers if necessary
}

# Payload
payload = {
    "lang": "en_US",
    "province": "ON",
    "type": 11,
    "page": 1
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Parse and print the response
if response.status_code == 200:
    response_data = json.loads(response.text)
    with open("out_put.json", "w") as f:
        json.dump(response_data, f, indent=4)
else:
    print(f"Failed to make the API call. Status code: {response.status_code}")
