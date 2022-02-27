import pymongo as pymongo


def connectdb():
    client = pymongo.MongoClient(
        "mongodb+srv://aida:ibragim23@cluster0.er4rz.mongodb.net/test?retryWrites=true&w=majority")

    db = client.test
    a = db.countries
    b = db.continents

    def find_country():
        user_input = str(input("Enter the letters"))

        for country in a.find({"Name": {'$regex': user_input,'$options': 'i'}}):

            print(country['Name'])

    find_country()


if __name__ == '__main__':
    connectdb()
