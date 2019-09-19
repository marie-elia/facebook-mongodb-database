import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

newImage =  { 
    "img_id": "firstimage",
    "image" : "firstimage.png",
    "caption" : "beach",
    "comments" : [ ], 
    "reactions": [ ]
}

condition = {
    'name' :'Marie Elia'
}

update = {
    "$push": {"pics" : newImage }
}

db.update_one(condition, update, upsert=True)


