import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

id =  "firstpost" 
number1 = {
    "name" : "Marie Elia", 
    "pics.img_id": "firstimage"
}
number2 = {
    "name" : "Marie Elia", 
    "posts.post_id": id
}

Comment1 = {
    "comment_id": "subcomimg", 
    "commenter": "Dalida",
    "text":"New subcomment",
    "reactions": []
}

Comment2 = {
    "comment_id": "subcompost", 
    "commenter": "Vidal",
    "text":"New subcomment!",
    "reactions": []
}

edit1 = {
    "$push": {"pics.0.comments.0.subcomments" : Comment1}
}
edit2 = {
    "$push": {"posts.0.comments.0.subcomments" : Comment2}
}

db.update_one(number1, edit1)
db.update_one(number2, edit2)




