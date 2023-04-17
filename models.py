from mongoengine import *

connect(host="mongodb://localhost:27017/web10")


class Authors(Document):
    fullname = StringField(max_length=70)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Authors)
    quote = StringField()
