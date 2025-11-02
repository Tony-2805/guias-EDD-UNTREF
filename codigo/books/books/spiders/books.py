import scrapy
from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "books"
    allowed_domain = ["books.toscrape.com"]
    start_urls = [
        "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"
    ]

    def parse(self, response):
        category = response.xpath("//div[@class='page-header action']/h1/text()")
        books = response.xpath("//article[@class='product_pod']")

        for b in books:
            item = BooksItem()

            item["title"] = b.xpath(".//h3/a/@title").get().strip()
            item["price"] =  int(b.xpath(".//p[@class='price_color']").get().strip()[1:])