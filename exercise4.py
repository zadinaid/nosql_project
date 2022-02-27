import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")

    db = client.test
    b = db.continents


    continents = b.find({}, {'Name': 1, 'countries': {'$slice': 4}}).sort("Name")

    for FourCountries in continents:
        print(FourCountries)


if __name__ == '__main__':
    connectdb()