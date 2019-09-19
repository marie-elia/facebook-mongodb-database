import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts


condition = {
    "name" : "Marie Elia", 
    "pics.img_id": "firstimage"
}

Comment = {
    "comment_id": "picture", 
    "commenter": "Claudine",
    "text":"Here we go!",
    "subcomments": [],
    "reactions": []
}
update = {
    "$push": {"pics.0.comments" : Comment}
}

db.update_one(condition, update)




