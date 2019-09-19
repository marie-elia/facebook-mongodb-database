import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

id = "pic" 

number1 = {
    "name" : "Marie Elia", 
    "pics.0.reactions.reaction_id": id
}
number2 = {
    "name" : "Marie Elia", 
    "posts.0.reactions.reaction_id": id
}
number3 = {
    "name" : "Marie Elia", 
    "pics.0.comments.0.reactions.reaction": id
}
number4 = {
    "name" : "Marie Elia", 
    "posts.0.comments.0.reactions.reaction": id
}
number5 = {
    "name" : "Marie Elia", 
    "pics.0.comments.0.subcomments.0.reactions.reaction": id
}
number6 = {
    "name" : "Marie Elia", 
    "posts.0.comments.0.subcomments.0.reactions.reaction": id
}


edit1 = {
    "$pop": {"pics.0.reactions" : -1 }
}
edit2 = {
    "$pop": {"posts.0.reactions" : -1 }
}
edit3 = {
    "$pop": {"pics.0.comments.0.reactions" : -1 }
}
edit4 = {
    "$pop": {"posts.0.comments.0.reactions" : -1 }
}
edit5 = {
    "$pop": {"pics.0.comments.0.subcomments.0.reactions" : -1 }
}
edit6 = {
    "$pop": {"posts.0.comments.0.subcomments.0.reactions" : -1}
}


db.update_one(number1, edit1, False)
db.update_one(number2, edit2, False)
db.update_one(number3, edit3, False)
db.update_one(number4, edit4, False)
db.update_one(number5, edit5, False)
db.update_one(number6, edit6, False)




