# Hacker News RSS Feed Reader 
_Build 1.0_

## **Setup Instructions**
---
#### Install Dependencies

`cd {Hacker News directory folder}`

_For Pip2_
`pip install setup.py`

_For Pip3_
`pip3 install setup.py`

#### MongoDB
_Official MongoDB Installtion Guide_

<a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-windows/">Window</a>

<a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-os-x/">Mac</a>

<a href="https://docs.mongodb.com/manual/administration/install-enterprise-linux/">Linux</a>

#### Configure Script with MongoDB

Search for `#Connect To Your Mongo DB` in `pipe.py`


Change `{DataBaseName}` to your MongoDB Database Name
Change `{CollectionName}` to your MongoDB Collection Name
`client = MongoClient()`
`db = client.{DataBaseName}`
`collection = db.{CollectionName}`

#### Running the script

Run `main.py` file.

## **Features**
---
* **Fetch Articles from Hacker News RSS Feed & Store in Mongo DB**
* **List Articles by ID**
* **View Individual Articles**
* **Open Articles in Browser**
* **Open Comment Sections in Browser**