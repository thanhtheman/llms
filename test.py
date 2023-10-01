import requests, os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

url = "https://api.elevenlabs.io/v1/voices"

headers = {
  "Accept": "application/json",
  "xi-api-key": os.getenv("ELEVENLABS_API")
}
response = requests.get(url, headers=headers)
with open("elevenLabsVoices.json", "w") as f:
  f.write(response.text)
