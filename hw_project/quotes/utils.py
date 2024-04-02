from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        'mongodb+srv://tsarevycholha:Rk3f448t5vpuTHu3@newcluster.w9thwg8.mongodb.net/?retryWrites=true&w=majority&appName=NewCluster')

    db = client.hw
    return db

