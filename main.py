import read
from write import Counter


def into():
    search = read.Search()
    while True:
        command = input("Введите команду (или '--help' для справки): ").lower()
        if command == "--help":
            print(
                "Команды:\n--top: Популярные запросы\nactor: "
                "Выполнить поиск по имени актера\nyear: Выполнить поиск по году фильма\nkeyword: "
                "Поиск по ключевому слову\ndescription: Вывод по описанию\ntitle: Выполнить "
                "поиск по названию фильма\ncategory: Выполнить поиск по категории ")
        elif command == "title":
            title = input("Введите название фильма: ").lower()
            search.search_by_title(title)
            counter = Counter(title)
            counter.insert_or_update()
            counter.close()
        elif command == "year":
            year = input("Введите год: ").lower()
            search.search_by_year(year)
            counter = Counter(year)
            counter.insert_or_update()
            counter.close()
        elif command == "exit":
            break
        elif command == 'actor':
            actor = input('Введите имя или фамилию актера: ').lower()
            search.search_by_actor(actor)
            counter = Counter(actor)
            counter.insert_or_update()
            counter.close()
        elif command == 'description':
            description = input('Введите слово(а): ').lower()
            search.search_by_description(description)
            counter = Counter(description)
            counter.insert_or_update()
            counter.close()


into()
