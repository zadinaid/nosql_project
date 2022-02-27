import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")
    
    db = client.test

    a = db.countries
    b = db.continents


    def look_for_u():

        for continents in a.find({
                    'Name':
                        {'$regex': 'u', '$options': 'i'}, 'Population': {'$gt': 100000}
                }

        ).sort("population"):

            print( continents['Name'], continents['Population'])

    look_for_u()


if __name__ == '__main__':
    connectdb()
