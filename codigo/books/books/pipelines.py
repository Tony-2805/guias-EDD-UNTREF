# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter



class CheapestBookPipeline:
    def __init__(self):
        self.cheapest = {}

    def process_item(self, item, spider):
        cat = item["category"]
        price = item["price"]

        if price < self.cheapest.get(cat, {}).get("price", float('inf')):
            self.cheapest[cat] = {
                "category": cat,
                "title": item["title"],
                "price": price,
                "availability": item["availability"],
            }

        return item
    
    def close_spider(self, spider):
        # Guardar el resultado al final
        data = list(self.cheapest.values())
        with open("../../datos/scrapy/cheapest_books.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
