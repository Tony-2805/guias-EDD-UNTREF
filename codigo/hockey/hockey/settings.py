# Scrapy settings for hockey project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "hockey"

SPIDER_MODULES = ["hockey.spiders"]
NEWSPIDER_MODULE = "hockey.spiders"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    "hockey.pipelines.HockeyPipeline": 300,
}

# Concurrency and throttling settings
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = 0.5

USER_AGENT = "hockey_scraper/1.0 (antonidonke.rep@gmail.com)"
LOG_LEVEL = "INFO"