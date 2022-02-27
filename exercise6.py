import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")
    
    db = client.test
    
    a = db.countries
    b = db.continents


    def population_order():

        for countries in a.find({}).sort("Population"):

            print(countries['Name'], countries['Population'])

    population_order()


if __name__ == '__main__':
    connectdb()