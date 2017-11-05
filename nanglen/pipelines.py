# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class NanglenPipeline(object):
#     def process_item(self, item, spider):
#         return item

import pymongo
import datetime

class MoviePipeline(object):

    collection_name = 'movies'
    today = datetime.datetime.now()
    current_year = str(today.year)
    if today.month < 10:
        current_month = '0' + str(today.month)
    else:
        current_month = str(today.month)

    if today.day < 10:
        current_day = '0' + str(today.day)
    else:
        current_day = str(today.day)
    
    current_date = current_year + current_month + current_day

    def __init__(self, mongo_server, mongo_port, mongo_db):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_uri = mongo_server + ":" + str(mongo_port)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGO_SERVER'),
            mongo_port=crawler.settings.get('MONGO_PORT'),
            mongo_db=crawler.settings.get('MONGO_DB', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        movie_collection = self.db[self.collection_name]
        found_movie = movie_collection.find_one({'Title': item['Title'], 'Year': item['Year']})
        item['LastOnAir'] = self.current_date
        if found_movie is None:
            movie_collection.insert_one(dict(item))
            return item
        else:
            movie_collection.find_one_and_update({'_id': found_movie['_id']}, {
                '$set': {'LastOnAir': self.current_date}
            })
            return item
