import scrapy, json


class HousespiderSpider(scrapy.Spider):
    name = "housespider"
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
    }
    
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
    
    def start_requests(self):
        url = 'https://housesigma.com/bkv2/api/search/homepage/recommendlist_v2'
        payload = {
            "lang": "en_US",
            "province": "ON",
            "type": 11,
            "page": 1
        }
        yield scrapy.Request(
            url,
            method='POST',
            headers=self.headers,
            body=json.dumps(payload),
            callback=self.parse
        )

    def parse(self, response):
        data = json.loads(response.text)
        with open("output.json", "w") as f:
            json.dump(data, f, indent=4)
