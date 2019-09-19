import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

id =  "subcompost"
id2="subcomimg"

number1 = {
    "name" : "Marie Elia", 
    "pics.0.comments.comment_id": id2
}
number2 = {
    "name" : "Marie Elia", 
    "posts.0.comments.comment_id": id
}
number3 = {
    "name" : "Marie Elia", 
    "pics.0.comments.0.subcomments.comment_id": id2
}
number4 = {
    "name" : "Marie Elia", 
    "posts.0.comments.0.subcomments.comment_id": id
}

edit1 = {
    "$set": {"pics.0.comments.0.text" : "edited image comment" }
}
edit2 = {
    "$set": {"posts.0.comments.0.text" : "edited post comment" }
}
edit3 = {
    "$set": {"pics.0.comments.0.subcomments.0.text" : "edited image subcomment" }
}
edit4 = {
    "$set": {"posts.0.comments.0.subcomments.0.text" : "edited post subcomment" }
}

db.update_one(number1, edit1, False)
db.update_one(number2, edit2, False)
db.update_one(number3, edit3, False)
db.update_one(number4, edit4, False)




