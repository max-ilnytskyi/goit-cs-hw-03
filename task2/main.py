from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.collection import Collection

initial_data = [
    {
        "name": "Lama",
        "age": 2,
        "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
    },
    {
        "name": "Liza",
        "age": 4,
        "features": ["ходить в лоток", "дає себе гладити", "білий"],
    },
    {
        "name": "Boris",
        "age": 12,
        "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
    },
    {
        "name": "Murzik",
        "age": 1,
        "features": ["ходить в лоток", "дає себе гладити", "чорний"],
    },
]

client = MongoClient(
    "mongodb://root:example@localhost:27017/cs_hw_03?authSource=admin",
    server_api=ServerApi("1"),
)

db = client.cs_hw_03
cats = db.cats


def seed(collection: Collection, data):
    delete_result = collection.delete_many({})
    if delete_result.deleted_count > 0:
        print(f"{delete_result.deleted_count} documents deleted")
    insert_result = collection.insert_many(data)
    print(f"{len(insert_result.inserted_ids)} documents created")


def read_all(collection: Collection):
    result = collection.find({})
    print("All documents:")
    for document in result:
        print(document)


def read_by_name(collection: Collection, name):
    result = collection.find({"name": name})
    print(f"Documents with name {name}:")
    for document in result:
        print(document)


def update_age_by_name(collection: Collection, name, age):
    result = collection.update_one({"name": name}, {"$set": {"age": age}})
    if result.modified_count > 0:
        print("Document updated")


def add_feature_by_name(collection: Collection, name, feature):
    result = collection.update_one({"name": name}, {"$addToSet": {"features": feature}})
    if result.modified_count > 0:
        print("Feature added")


def delete_by_name(collection: Collection, name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Document deleted")


def delete_all(collection: Collection):
    result = collection.delete_many({})
    if result.deleted_count > 0:
        print(f"{result.deleted_count} documents deleted")


if __name__ == "__main__":
    seed(cats, initial_data)

    read_all(cats)

    read_by_name(cats, "Murzik")

    update_age_by_name(cats, "Lama", 5)

    add_feature_by_name(cats, "Liza", "сірий")

    delete_by_name(cats, "Boris")

    delete_all(cats)
