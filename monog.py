# def get_database():
#     from pymongo import MongoClient
#     import pymongo

#     # Provide the mongodb atlas url to connect python to mongodb using pymongo
#     CONNECTION_STRING = (
#         "mongodb+srv://crlough:wakaflocka@cluster0.cqd6b.mongodb.net/homework5db"
#     )

#     # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
#     from pymongo import MongoClient

#     client = MongoClient(CONNECTION_STRING)

#     # Create the database for our example (we will use the same database throughout the tutorial
#     return client["hw_db"]


# # This is added so that many files can reuse the function get_database()
# if __name__ == "__main__":
#     import pandas as pd
#     from pprint import pprint

#     # Get the database
#     db = get_database()
#     # users_collection = db["users"]

#     # load_dict = pd.read_csv("accounts.csv")
#     # load_dict.columns = load_dict.columns.str.lower()
#     # load_dict = load_dict.to_dict(orient="records")

#     # users_collection.insert_many(load_dict)
#     row = db.users.find_one({"user_id": "Brittaney.Gentry86"})
#     pprint(row)
#     # item_details = collection_name.find()
#     # items_df = pd.DataFrame(item_details)
#     # print(items_df)
import main
from pprint import pprint

db = main.get_database()
row = db.users.find_one({"user_id": "Keri.Royce8"})
pprint(row)
