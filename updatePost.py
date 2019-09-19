import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

number = {
    "posts.post_id" : "firstpost"
}

edit = {
    "$set": {"posts.0.text" : "Updated my first post" }
}


db.update_one(number, edit)
