# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class HockeyPipeline:
    def __init__(self):
        self.best_teams = {}
    def process_item(self, item, spider):
        year = item["year"]
        name = item["name"]
        wins = item["wins"]

        if wins > self.best_teams.get(year, ("", 0))[1]:
            self.best_teams[year] = (name,wins)
        
        return item
    
    def close_spider(self, spider):
        """Se ejecuta cuando se cierra el spider"""
        resultados = [
            {"year": year, "name": name, "wins": wins}
            for year, (name, wins) in self.best_teams.items()
        ]

        # Guardar archivo en la carpeta ./datos/scrapy/
        with open("../../datos/scrapy/hockey_teams.json", "w", encoding="utf-8") as f:
            import json
            json.dump(resultados, f, ensure_ascii=False, indent=2)
