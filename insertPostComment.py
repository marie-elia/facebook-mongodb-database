import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

condition = {
    "name" : "Marie Elia", 
    "posts.post_id":  "firstpost"
}

Comment = {
    "comment_id": "poster", 
    "commenter": "Milania",
    "text":"Great",
    "subcomments": [],
    "reactions": []
}
update = {
    "$push": {"posts.0.comments" : Comment}
}

db.update_one(condition, update)




