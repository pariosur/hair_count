from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://pabloriosur:<password>@unilaser.61szfku.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('hairdata')
user_collection = pymongo.collection.Collection(db, 'unilaser')
