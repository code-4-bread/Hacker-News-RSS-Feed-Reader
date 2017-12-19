import feedparser, datetime
from pymongo import MongoClient

client = MongoClient()
db = client.HKN
collection = db.NewsCollection

url = 'https://news.ycombinator.com/rss'
feed = feedparser.parse(url)
for item in feed['items']:
    if collection.count({'title' : item['title']}) == 0:
        collection.insert_one({
            'title' : item['title'],
            'link_to_article' : item['link'],
            'published_date' : item['published'],
            'link_to_comments' : item['comments'],
            'created_datetime' : datetime.datetime.utcnow()
        })








