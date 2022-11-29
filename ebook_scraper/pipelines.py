from pymongo import MongoClient
from itemadapter import ItemAdapter
class EbookScraperPipeline:

    def open_spider(self, spider):
        self.client = MongoClient(
            host="mongodb+srv://Nick:Fyzmy1ME1Z3T4kiL@ebookscraper.mgcekl1.mongodb.net/?retryWrites=true&w=majority",
            connect=False
        )
        self.collection = self.client.get_database("ebook").get_collection("travel")

    def process_item(self, item, spider):
        self.collection.insert_one(
            ItemAdapter(item).asdict()
        )
        return item

    def close_spider(self, spider):
        self.client.close()