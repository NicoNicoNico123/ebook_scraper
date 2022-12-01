import scrapy
# from ebook_scraper.items import EbookItem
# from scrapy.loader import ItemLoader

class EbookSpider(scrapy.Spider):
    name="ebook"
    start_urls = [ "https://www.scrapethissite.com/pages/advanced/?gotcha=csrf" ]

    def parse(self, response):
        csrf_token = response.css("input[name='csrf']").attrib["value"]
        print(
            "[CSRF]:",
           csrf_token
        )

        yield scrapy.FormRequest(
            "https://www.scrapethissite.com/pages/advanced/?gotcha=csrf",
            formdata={
                "user": "test",
                "pass": "test",
                "csrf": csrf_token
            },
            callback=self.parse_login
        )
    
    def parse_login(self, response):
        print("[ Result ]:", response.css("div.row div::text").get())
    # def parse(self, response):
    #     table= response.css("table")

    #     product_details = {}
    #     for row in table.css("tr"):

    #         heading = row.css("th::text").get()
    #         data = row.css("td::text").get()

    #         product_details[heading] = data

    #     yield product_details
