import pymongo
from pymongo import MongoClient
cluster = MongoClient()
db = cluster["database"]
collection = db["customer"]
data = {"name":"can","age":"21"}
collection.insert_one(data)