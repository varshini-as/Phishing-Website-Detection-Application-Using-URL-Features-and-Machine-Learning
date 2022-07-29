
import pymongo

client = pymongo.MongoClient('mongodb+srv://majorproject:project12345@cluster0.e90mk.mongodb.net/URL_Blacklist?retryWrites=true&w=majority')

# connect to DB
db = client['URL_Blacklist']  

# connect to collection in DB
collection = db['URL_Blacklist']

def addURL_MongoDB(url): # add new URL to DB
    data = {'url' : url}
    collection.insert_one(data)

def search_URL(url):   # search user input URL in database
    found = collection.find({'url' : url})
    # print(found)
    exists = True
    if found:
        for result in found:
            return exists
        exists = False
    return exists

print(search_URL('http://shadetreetechnology.com/V4/validation/a111aedc8ae390eabcfa130e041a10a4'))

