import datetime
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

condition = {
    "name" : "Marie Elia"
}

update = {
    "$set" : {"password" : "2389"}
}

db.update_one(condition, update, upsert=False)