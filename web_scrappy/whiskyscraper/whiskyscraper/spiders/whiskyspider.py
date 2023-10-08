import scrapy


class WhiskyspiderSpider(scrapy.Spider):
    name = "whiskyspider"
    allowed_domains = ["www.whiskyshop.com"]
    start_urls = ["https://www.whiskyshop.com/blended-scotch-whisky?item_availability=In+Stock"]

    def parse(self, response):
        try:
            for item in response.css("div.product-item-info"):
                yield {
                    "name": item.css("a.product-item-link::text").get(),
                    "price": item.css("span.price::text").get(),
                    "link": item.css("a.product-item-link").attrib["href"],
                    "image": item.css("img.product-image-photo").attrib["src"]
                }
        except:
            for item in response.css("div.product-item-info"):
                yield {
                    "name": item.css("a.product-item-link::text").get(),
                    "price": item.css("span.price::text").get(),
                    "link": item.css("a.product-item-link").attrib["href"],
                    "image": item.css("img.product-image-photo").attrib.get("data-original", None)
                }

        # next_page = response.css("a.action.next").attrib["href"]
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
        # else:
        #     print("No more pages")