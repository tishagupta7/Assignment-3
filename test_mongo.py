import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)

db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

test_transaction = {
    "transaction_id": "TEST001",
    "customer_id": "CUST001",
    "amount": 5000,
    "merchant": "Amazon",
    "is_fraud": False
}

result = collection.insert_one(test_transaction)

print("MongoDB Atlas connected successfully!")
print("Document inserted successfully!")
print("Inserted ID:", result.inserted_id)

client.close()