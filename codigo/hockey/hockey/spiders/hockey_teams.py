import scrapy
from hockey.items import HockeyItem

class HockeyTeamsSpider(scrapy.Spider):
    name = "hockey_teams"
    allowed_domains = ["scrapethissite.com"]
    start_urls = [
        "https://www.scrapethissite.com/pages/forms/?page_num=1"
    ]

    def parse(self, response):
        teams = response.xpath("//tr[@class = 'team']")
        
        for team in teams:
            act = HockeyItem()
        
            act["year"] = team.xpath(".//td[@class='year']/text()").get(default="").strip()
            act["name"] = team.xpath(".//td[@class='name']/text()").get(default="").strip()
            act["wins"] = int(team.xpath(".//td[@class='wins']/text()").get(default="0").strip())

            yield act

        next_page = response.xpath(
            "//ul[contains(@class,'pagination')]//a[@aria-label='Next']/@href").get()
        
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)