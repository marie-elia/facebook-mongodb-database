import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

condition = {
    "pics.img_id" : "firstimage"
}

update = {
    "$pop": {"pics" : -1 }
}


db.update_one(condition, update)
