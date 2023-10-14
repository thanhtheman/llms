import httpx, random
from bs4 import BeautifulSoup

url = "https://www.zolo.ca/toronto-real-estate/page-1"

user_agent_list = [{"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3'},
                {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0"},
                {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15"},
                {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"},
                {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
                ]
user_agent = random.choice(user_agent_list)

# r = httpx.get(url, headers=user_agent)

# with open("home.html", "w") as f:
#     f.write(r.text)

soup = BeautifulSoup(open("pretty.html"), "html.parser")
# with open("pretty.html", "w") as f:
#     f.write(soup.prettify())
print(soup.find_all("article"))
