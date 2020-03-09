# -*- coding: utf-8 -*-

from dateutil import parser
from datetime import datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.NewsAPI
collection = db.Articles
articles = collection.find({'publishedAt': {'$exists':True}})

for article in articles:
    if isinstance(article['publishedAt'], str):
        publishedAt = article['publishedAt']
        try:
            publishedAt = parser.parse(publishedAt)
        except:
            publishedAt = None
        collection.update_one({'_id': article['_id']},
                {'$set': {'publishedAt': publishedAt}},  True)
    