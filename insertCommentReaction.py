import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

id = "firstimage" 
number1 = {
    "name" : "Marie Elia", 
    "pics.img_id": id
}
number2 = {
    "name" : "Marie Elia", 
    "posts.post_id": id
}

react1 = {
    "reaction_id": "imgone", 
    "reaction": "Love",
    "reactor":"Marie Elia"
}
react2 = {
    "reaction_id": "postone", 
    "reaction": "Love",
    "reactor":"Marie Elia"
}

edit1 = {
    "$push": {"pics.0.comments.0.reactions" : react1}
}
edit2 = {
    "$push": {"posts.0.comments.0.reactions" : react2}
}

db.update_one(number1, edit1)
db.update_one(number2, edit2)




