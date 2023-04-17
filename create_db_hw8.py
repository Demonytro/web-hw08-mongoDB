from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://userweb10:567234@cluster0.eukkmyr.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'))
db = client.hw8
