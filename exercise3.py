import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")

    db = client.test

    a = db.countries
    b = db.continents

    def add_continents():

        agg_pipeline = [
        {
            '$project': {
                'name': "$name",
                'countries': {'$size': "$countries"}}
        }]

        c = b.aggregate(agg_pipeline)

        for continent in c:
            print(continent)

    add_continents()


if __name__ == '__main__':
    connectdb()