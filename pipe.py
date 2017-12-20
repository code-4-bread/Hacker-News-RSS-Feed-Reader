import feedparser, datetime, schedule, webbrowser, threading
from pymongo import MongoClient

#Connect To Your Mongo DB
client = MongoClient()
db = client.{DataBaseName}
collection = db.{CollectionName}

def spooler():
    thread = threading.Thread(target=fetch_update_15, args=())
    thread.daemon = True
    thread.start()

def doc_viewall():
    cur = collection.find({})
    for each in cur:
        print('ID - {} \nTitle - {}'.format(each['id'],each['title']))
        print(' ')

    choice_bool = True
    while choice_bool:
        choice = input('Available Commands\nOD - Open Document\nRE - Refresh The List\nFU - Force Update\n')
        if choice.upper() == 'OD':
            id = input('Please Enter the Article ID\n')
            doc_viewsingle(id)
            choice_bool = False
        elif choice.upper() == 'RE':
            doc_viewall()
            choice_bool = False
        elif choice.upper() == 'FU':
            fetch_update()
        else:
            print('Please enter avaiable commands')



def open_in_browser(url):
    webbrowser.open_new_tab(url)

def doc_viewsingle(id):
    exist = collection.count({'id': int(id)})
    print(exist)
    if exist == 0:
        print("Record Doesn't Exist")
        valid_input_bool = True
        while valid_input_bool:
            valid_input = input("Please enter the valid ID\nIf you wish to view all the Articles again, enter X\n")
            if valid_input.isdigit():
                doc_viewsingle(valid_input)
                valid_input_bool = False
            else:
                if valid_input.upper() == 'X':
                    doc_viewall()
                    valid_input_bool = False
                else:
                    valid_input = input("Please enter the valid ID\nIf you wish to view all the Articles again, enter X\n")
    elif exist > 0:
        cur = collection.find({'id':int(id)})
        print('Title - {}\nPublished Date - {}\nLink To Article - {}\nLink To Comments - {}'.format(cur[0]['title'],cur[0]['published_date'],cur[0]['link_to_article'],cur[0]['link_to_comments']))
        print('')
        choice_bool = True
        while choice_bool:
            choice = input('Available Commands\nVA - View All Articles\nO - Open Current Article in Browser\nOC - Open Comments in Browser\n')
            if choice.upper() == 'VA':
                doc_viewall()
                choice_bool = False
            elif choice.upper() == 'O':
                open_in_browser(cur[0]['link_to_article'])
                choice_bool = False
                doc_viewsingle(id)
            elif choice.upper() == 'OC':
                open_in_browser(cur[0]['link_to_comments'])
                choice_bool = False
                doc_viewsingle(id)
            else:
                print('')
                print('Invalid Input')
                print('')


def fetch_update():
    print('Upadting Database......')
    url = 'https://news.ycombinator.com/rss'
    feed = feedparser.parse(url)
    for item in feed['items']:
        count = collection.count()
        if collection.count({'title': item['title']}) == 0:
            count += 1
            collection.insert_one({
                'id' : count,
                'title': item['title'],
                'link_to_article': item['link'],
                'published_date': item['published'],
                'link_to_comments': item['comments'],
                'created_datetime': datetime.datetime.utcnow()
            })
    print('')
    print('Database Updated : ' + str(datetime.datetime.utcnow()))
    print('')

def fetch_update_15():
    schedule.every(15).minutes.do(fetch_update)

    while True:
        schedule.run_pending()