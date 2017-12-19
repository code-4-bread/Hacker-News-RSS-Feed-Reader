import pymongo
from pipe import *
import threading

def main():
    spooler()
    print('Hacker News RSS Feed Reader')
    print('*IF YOU ARE FIRST TIME RUNNING THIS, PLEASE FORCE UPDATE ARTICLES FIRST*')
    print('')

    choice = True
    while choice:
        choice = input('Available Commands\nVA - View All Articles\nFU - Force Update Articles\n')
        if choice.upper() == 'VA':
            doc_viewall()
            choice = False
        elif choice.upper() == 'FU':
            fetch_update()
        else:
            print('')
            print('Invalid Input')
            print('')

if __name__ == "__main__":
    main()