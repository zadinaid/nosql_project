import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")
    
    db = client.test
    a = db.countries
    b = db.continents

    a.update_one({'Name': 'Greece'}, {'$set': {'Population': 10339733}})
    a.update_one({'Name': 'France'}, {'$set': {'Population': 65513442}})
    a.update_one({'Name': 'Great Britain'}, {'$set': {'Population': 68482219}})
    a.update_one({'Name': 'Kazakhstan'}, {'$set': {'Population': 19157610}})


if __name__ == '__main__':
    connectdb()