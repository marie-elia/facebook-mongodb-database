import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

post =  { 
    "post_id": "firstpost",
    "text" :"Welcome to facebook",
    "dateCreated" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "comments" : [ ], 
    "reactions": [ ]
}

condition = {
    'name' :'Marie Elia'
}

update = {
    "$push": {"posts" : post}
}

db.update_one(condition, update, upsert=True)


