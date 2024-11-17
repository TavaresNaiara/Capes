from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["dashboard_db"]
history_collection = db["search_history"]


history_collection.insert_one({"user_id": "123", "query": "IA", "timestamp": "2024-11-17"})


history = history_collection.find({"user_id": "123"})
for record in history:
    print(record)
