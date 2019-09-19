import datetime
import pymongo
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

condition = {
    "name" : "Marie Elia"
}

db.delete_one(condition)