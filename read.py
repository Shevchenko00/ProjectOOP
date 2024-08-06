from connector import ConnectorRead


class Search:
    def __init__(self):
        self.connection = ConnectorRead.get_connect()
        self.cursor = self.connection.cursor()

    def result_print(self, data):
        for i in data:
            print(
                f'Title: {i[1]}\tDescription: {i[2]}\tYear: {i[3]}\tCategory: '
                f'{i[4]}\tActor Name: {i[5]}\tActor Surname: {i[6]}')

    def search_by_title(self, query):
        select = f"""select distinct
        t1.film_id, t1.title, t1.description, t1.release_year, 
        t3.name as category_name, 
        t5.first_name, t5.last_name
        from film as t1
        left join film_category as t2 on t1.film_id = t2.film_id
        left join category as t3 on t3.category_id = t2.category_id
        left join film_actor as t4 on t1.film_id = t4.film_id
        left join actor as t5 on t4.actor_id = t5.actor_id
        where t1.title like '%{query}%'
        """
        self.cursor.execute(select)
        data = self.cursor.fetchall()
        self.result_print(data)
        return data

    def search_by_year(self, year):
        select = f"""select distinct
        t1.film_id, t1.title, t1.description, t1.release_year, 
        t3.name as category_name, 
        t5.first_name, t5.last_name
        from film as t1
        left join film_category as t2 on t1.film_id = t2.film_id
        left join category as t3 on t3.category_id = t2.category_id
        left join film_actor as t4 on t1.film_id = t4.film_id
        left join actor as t5 on t4.actor_id = t5.actor_id
        where t1.release_year = '{year}'
        """
        self.cursor.execute(select)
        data = self.cursor.fetchall()
        self.result_print(data)
        return data

    def search_by_actor(self, name):
        select = f"""select distinct
        t1.film_id, t1.title, t1.description, t1.release_year, 
        t3.name as category_name, 
        t5.first_name, t5.last_name
        from film as t1
        left join film_category as t2 on t1.film_id = t2.film_id
        left join category as t3 on t3.category_id = t2.category_id
        left join film_actor as t4 on t1.film_id = t4.film_id
        left join actor as t5 on t4.actor_id = t5.actor_id
        where t5.first_name like '%{name}%' or t5.last_name like '%{name}%'
        """
        self.cursor.execute(select)
        data = self.cursor.fetchall()
        self.result_print(data)
        return data

    def search_by_description(self, description):
        select = f"""select distinct
                t1.film_id, t1.title, t1.description, t1.release_year, 
                t3.name as category_name, 
                t5.first_name, t5.last_name
                from film as t1
                left join film_category as t2 on t1.film_id = t2.film_id
                left join category as t3 on t3.category_id = t2.category_id
                left join film_actor as t4 on t1.film_id = t4.film_id
                left join actor as t5 on t4.actor_id = t5.actor_id
                where t1.description like '%{description}%' limit 15
                """
        self.cursor.execute(select)
        data = self.cursor.fetchall()
        self.result_print(data)
        return data

    def search_by_keyword(self, keyword):
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
        where title like '%{keyword}%' or
        description like '%{keyword}%' or
        release_year like '%{keyword}%' or
        first_name like '%{keyword}%' or
        name like '%{keyword}%' limit 15;
        """
        self.cursor.execute(select)
        self.data = self.cursor.fetchall()
        self.result_print()
        return self.data

    def search_by_category(self, category):
        select = f"""select distinct
        t1.film_id, t1.title, t1.description, t1.release_year, 
        t3.name as category_name, 
        t5.first_name, t5.last_name
        from film as t1
        left join film_category as t2 on t1.film_id = t2.film_id
        left join category as t3 on t3.category_id = t2.category_id
        left join film_actor as t4 on t1.film_id = t4.film_id
        left join actor as t5 on t4.actor_id = t5.actor_id
        where t3.name like '%{category}%' limit 15
                        """
        self.cursor.execute(select)
        data = self.cursor.fetchall()
        self.result_print(data)
        return data


def main():
    search = Search()
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
        elif command == "year":
            year = input("Введите год: ").lower()
            search.search_by_year(year)
        elif command == "exit":
            break
        elif command == 'actor':
            actor = input('Введите имя или фамилию актера: ').lower()
            search.search_by_actor(actor)
        elif command == 'description':
            description = input('Введите слово(cловa) для поиска по описанию : ').lower()
            search.search_by_description(description)
        elif command == 'keyword':
            keyword = input('Введите ключевое слово: ').lower()
            search.search_by_keyword(keyword)
        elif command == 'category':
            category = input('Введите категорию: ').lower()
            search.search_by_category(category)
        else:
            print("Неверная команда. Введите '--help' для справки.")


if __name__ == "__main__":
    main()
