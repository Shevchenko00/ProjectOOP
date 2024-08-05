from connector import ConnectorRead

into = input("Введите команду: ")
if into == "--help":
    print(
        "Команды:\n--top: Популярные запросы\nactor: "
        "Выполнить поиск по имени актера\nyear: Выполнить поиск по году фильма\nkeyword: "
        "Поиск по ключевому слову\ndescription: Вывод по описанию\ntitle: Выполнить "
        "поиск по названию фильма\ncategory: Выполнить поиск по категории ")
elif into == "actor":
    actor = input('Введите имя актера: ')
elif into == "year":
    year = input("Введите год: ")
elif into == "keyword":
    keyword = input("Введите ключевое слово: ")
elif into == 'description':
    description = input('Введите описание: ')
elif into == 'title':
    title = input("Введите название фильма: ")
elif into == "category":
    category = input("Введите назввание категории")


# --help --top, actor ,year, keyword, description, category


class Search:
    def __init__(self, query):
        self.query = query
        self.connection = ConnectorRead.get_connect()
        self.cursor = self.connection.cursor()

    def result_print(self):
        for i in self.data:
            print(f'{i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[-1]}')

    #     self.connection = ConnectorRead.get_connect()
    #     self.cursor = self.connection.cursor()

    def get_result_search(self):
        cursor = self.connection.cursor()
        select = f"""select distinct
 t1.film_id, t1.title, t1.description, t1.release_year, 
t3.name as name, 
 t5.first_name, t5.last_name
from film as t1
left join film_category as t2
on t1.film_id = t2.film_id
left join category as t3
on t3.category_id = t2.category_id
left join film_actor as t4
on t1.film_id = t4.actor_id
left join actor as t5
on t4.actor_id = t5.actor_id
where title like '%{title}%' or 
description like '%{description}%' or 
release_year like '%{year}%' or
first_name like '%{actor}%' or
name like '%{category}%' limit 5000;
"""
        self.cursor.execute(select)
        self.data = self.cursor.fetchall()
        self.result_print()


search = Search
print(search.get_result_search())
