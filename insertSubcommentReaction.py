import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

id =   "firstpost" 
number1 = {
    "name" : "Marie Elia", 
    "pics.img_id": "firstimage"
}
number2 = {
    "name" : "Marie Elia", 
    "posts.post_id": id
}

React1 = {
    "reaction_id": "subreactimg", 
    "reaction": "Angry",
    "reactor":"Marie Elia"
}
React2 = {
    "reaction_id": "subreactpost", 
    "reaction": "Angry",
    "reactor":"Marie Elia"
}

update1 = {
    "$push": {"pics.0.comments.0.subcomments.0.reactions" : React1}
}
update2 = {
    "$push": {"posts.0.comments.0.subcomments.0.reactions" : React2}
}

db.update_one(number1, update1)
db.update_one(number2, update2)




