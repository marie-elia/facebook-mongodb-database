import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

number= {
    "pics.img_id" : "firstimage"
}

edit = {
    "$set": {"pics.0.caption" : "edited my first caption" }
}


db.update_one(condition, edit)
