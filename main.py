from mongoengine import *
import pymongo

from models import Authors, Quotes

connect(host="mongodb://localhost:27017/web10")


def find_by_name(a_pars):
    if a_pars:
        author = Authors.objects(fullname__startswith=a_pars[1])
        quotes = Quotes.objects(author=author[0].id)
        for quote in quotes:
            dict_res = quote.to_mongo().to_dict()
            print(dict_res.get("quote"))


def find_by_tags(a_pars: list):

    if a_pars:
        b = a_pars[1].strip().split(',')
        posts = Quotes.objects(tags__in=b)
        for post in posts:
            dict_res = post.to_mongo().to_dict()
            print(dict_res.get("quote"))


if __name__ == '__main__':
    while True:
        command_name = input('Принимает команды в следующем формате команда:значение >>> ')
        if command_name == "exit":
            break
        try:
            command_name_pars = command_name.strip().split(':')
            if command_name_pars[0] == 'name':
                find_by_name(command_name_pars)
            elif command_name_pars[0] == 'tags':
                find_by_tags(command_name_pars)

        except Exception as err:
            print(err)
