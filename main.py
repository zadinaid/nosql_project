import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")

    db = client.test

    a = db.countries
    b = db.continents

    print(db.list_collection_names())

    cursor = a.find({})
    for i in cursor:
        print(i)
    continent = b.find({})
    for a in continent:
        print(a)








