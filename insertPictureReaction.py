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

React = {
    "reaction_id": "pic", 
    "reaction": "Like",
    "reactor":"Marie Elia"
}
update = {
    "$push": {"pics.0.reactions" : React}
}

db.update_one(condition, update)




