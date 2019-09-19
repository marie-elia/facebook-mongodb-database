import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

condition = {
    "name" : "Marie Elia", 
    "posts.post_id":   "firstpost"
}

React = {
    "reaction_id": "postReaction", 
    "reaction": "Like",
    "reactor":"Marie Elia"
}
update = {
    "$push": {"posts.0.reactions" : React}
}

db.update_one(condition, update)




