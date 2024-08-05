from mongoengine import connect
from models import Author, Quote

uri = "mongodb+srv://Boris:ytunymuny@cluster0.nsntelu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Подключение к базе данных MongoDB Atlas
connect(host=uri)

def find_quotes_by_author(name):
    author = Author.objects(fullname=name).first()
    if author:
        quotes = Quote.objects(author=author)
        return [quote.text for quote in quotes]
    return []

def find_quotes_by_tag(tag):
    quotes = Quote.objects(tags=tag)
    return [quote.text for quote in quotes]

def find_quotes_by_tags(tags):
    tags_list = tags.split(',')
    quotes = Quote.objects(tags__in=tags_list)
    return [quote.text for quote in quotes]

def main():
    while True:
        command = input("Введите команду: ").strip()
        if command.lower() == "exit":
            print("Завершение работы.")
            break
        elif command.startswith("name:"):
            name = command[len("name:"):].strip()
            quotes = find_quotes_by_author(name)
            if quotes:
                print(f"Цитаты автора {name}:")
                for quote in quotes:
                    print(f"- {quote}")
            else:
                print(f"Цитат от {name} не найдено.")
        elif command.startswith("tag:"):
            tag = command[len("tag:"):].strip()
            quotes = find_quotes_by_tag(tag)
            if quotes:
                print(f"Цитаты с тегом {tag}:")
                for quote in quotes:
                    print(f"- {quote}")
            else:
                print(f"Цитат с тегом {tag} не найдено.")
        elif command.startswith("tags:"):
            tags = command[len("tags:"):].strip()
            quotes = find_quotes_by_tags(tags)
            if quotes:
                print(f"Цитаты с тегами {tags}:")
                for quote in quotes:
                    print(f"- {quote}")
            else:
                print(f"Цитат с тегами {tags} не найдено.")
        else:
            print("Неверная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
