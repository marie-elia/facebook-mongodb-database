import datetime
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.facebook.accounts

User =  { 
    "username" :"marie",
    "name" :"Marie Elia",
    "gender" : "Female",
    "age" : 23, 
    "email" :"marieelia@aucegypt.edu", 
    "password" :"123456", 
    "date" : datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    "posts" : [ ],
    "pics" : [ ] , 
    "profilepic" : { }
}

db.insert_one(User)

