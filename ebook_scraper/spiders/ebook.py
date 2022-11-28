import scrapy

class EbookSpider(scrapy.Spider):
    name="ebook"
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        print("[parse]")

        title = response.css("h3 a::text").get()
        price = response.xpath("//p[@class = 'price_color']").get()
