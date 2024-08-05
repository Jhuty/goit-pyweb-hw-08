from mongoengine import Document, StringField, BooleanField, ListField, ReferenceField, connect, CASCADE
from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://Boris:ytunymuny@cluster0.nsntelu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

connect(host=uri)


class Contact(Document):
    fullname = StringField(required=True, max_length=200)
    email = StringField(required=True, unique=True)
    message_sent = BooleanField(default=False)
    