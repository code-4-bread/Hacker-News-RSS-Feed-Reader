import feedparser, datetime, schedule
from pymongo import MongoClient


client = MongoClient()
db = client.HKN
collection = db.NewsCollection

def get_document_by_id():
    pass

def save_document():
    pass

def fetch_update():
    url = 'https://news.ycombinator.com/rss'
    feed = feedparser.parse(url)
    for item in feed['items']:
        if collection.count({'title': item['title']}) == 0:
            collection.insert_one({
                'title': item['title'],
                'link_to_article': item['link'],
                'published_date': item['published'],
                'link_to_comments': item['comments'],
                'created_datetime': datetime.datetime.utcnow()
            })

    print('Database Updated : ' + str(datetime.datetime.utcnow()))

def fetch_update_15():
    schedule.every(1).minutes.do(fetch_update)

    while True:
        schedule.run_pending()