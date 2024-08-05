import json
from models import Author, Quote

# Загрузка авторов
with open('D:\GoIT Python Software Engineer\goit-pyweb-hw-08.1/authors.json', 'r') as f:
    authors_data = json.load(f)

# Загрузка цитат
with open('D:\GoIT Python Software Engineer\goit-pyweb-hw-08.1/qoutes.json', 'r') as f:
    quotes_data = json.load(f)

# Сохранение авторов
author_objects = {}
for author in authors_data:
    author_obj = Author(
        fullname=author['fullname'],
        born_date=author.get('born_date', ''),
        born_location=author.get('born_location', ''),
        description=author.get('description', '')
    ).save()
    author_objects[author['fullname']] = author_obj

# Сохранение цитат
for quote in quotes_data:
    author_name = quote['author']
    author_obj = author_objects.get(author_name)
    if author_obj:
        Quote(
            text=quote['quote'],
            author=author_obj,
            tags=quote.get('tags', [])
        ).save()
