from pymongo import MongoClient
conn = MongoClient(host="localhost",port=27017)
db = conn['db_Nition']