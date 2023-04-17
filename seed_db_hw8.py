import mongoengine
import json
import pymongo

from models import Authors, Quotes

if __name__ == '__main__':
    with open('authors.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            author = Authors(fullname=i.get('fullname'),
                             born_date=i.get('born_date'),
                             born_location=i.get('born_location'),
                             description=i.get('description')) \
                .save()

    with open('quotes.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in data:
            author = Authors.objects(fullname=i.get('author', None)).first()
            quote = Quotes(tags=i.get('tags'),
                           author=author,
                           quote=i.get('quote')) \
                .save()
