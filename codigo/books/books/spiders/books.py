import scrapy
from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/"
    ]

    def parse(self, response):
        categories = response.xpath("//ul[@class='nav nav-list']//ul//a/@href").getall()
        for c in categories:
            url = response.urljoin(c)
            yield scrapy.Request(url, callback=self.parse_books)



    def parse_books(self,response):
        category = response.xpath("//div[@class='page-header action']/h1/text()").get().strip()
        if not category:
            category = "Desconocida"
            
        books = response.xpath("//article[@class='product_pod']")

        for b in books:
            item = BooksItem()

            item["title"] = b.xpath(".//h3/a/@title").get().strip()
            item["price"] =  float(b.xpath(".//p[@class='price_color']/text()").get().strip()[1:])
            item["category"] = category
            availability = b.xpath(
                ".//p[contains(@class,'instock') and contains(@class,'availability')]/text()"
            ).getall()
            item["availability"] = (
                "".join(availability).strip() if availability else None
            )

            yield item
        
        next_page = response.xpath("//li[contains(@class,'next')]/a/@href").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse_books)
        