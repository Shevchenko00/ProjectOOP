from connector import ConnectorWrite
import read


class Counter:
    def __init__(self, query):
        self.query = query
        self.connection = ConnectorWrite.get_connect()
        self.cursor = self.connection.cursor()

    def select(self):
        self.cursor.execute("SELECT * FROM 310524ptm_O_Shevchenko.query_results WHERE query = %s;",
                            (self.query,))  # Не баг, а фича
        self.result = self.cursor.fetchall()
        return self.result

    def close(self):
        self.cursor.close()
        self.connection.close()


class InsertTo:
    def __init__(self, query):
        self.query = query
        self.connection = ConnectorWrite.get_connect()
        self.cursor = self.connection.cursor()

    def insert_or_update(self):
        self.cursor.execute("SELECT * FROM 310524ptm_O_Shevchenko.query_results WHERE query = %s;", (self.query,))
        result = self.cursor.fetchall()
        if len(result) > 0:
            self.cursor.execute("UPDATE query_results SET count = %s WHERE id = %s", (result[0][-1] + 1, result[0][0]))
        else:
            self.cursor.execute("INSERT INTO query_results (query, count) VALUES (%s, %s)", (self.query, 1))
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()


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
            insert_to = InsertTo(title)
            insert_to.insert_or_update()
            insert_to.close()
        elif command == "year":
            year = input("Введите год: ").lower()
            search.search_by_year(year)
            insert_to = InsertTo(year)
            insert_to.insert_or_update()
            insert_to.close()
        elif command == "exit":
            break
        elif command == 'actor':
            actor = input('Введите имя или фамилию актера: ').lower()
            search.search_by_actor(actor)
            insert_to = InsertTo(actor)
            insert_to.insert_or_update()
            insert_to.close()
        elif command == 'description':
            description = input('Введите слово(cловa: )')


into()
