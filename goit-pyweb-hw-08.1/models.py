from mongoengine import Document, StringField, ListField, ReferenceField, connect, CASCADE
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://Boris:ytunymuny@cluster0.nsntelu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


connect(host=uri)
        
class Author(Document):
    fullname = StringField(required=True, max_length=200)
    born_date = StringField(max_length=100)
    born_location = StringField(max_length=200)
    description = StringField()


class Quote(Document):
    text = StringField(required=True)
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))

