from connector import get_write_connection


class Counter:
    def __init__(self, query):
        self.query = query
        self.connection = get_write_connection()  # Вызов функции для получения соединения
        self.cursor = self.connection.cursor()  # Инициализация курсора

    def select(self):
        self.cursor.execute("SELECT * FROM 310524ptm_O_Shevchenko.query_results WHERE query = %s;",
                            (self.query,))
        return self.cursor.fetchall()

    def insert_or_update(self):
        self.cursor.execute("SELECT * FROM 310524ptm_O_Shevchenko.query_results WHERE query = %s;",
                            (self.query,))
        result = self.cursor.fetchall()
        if len(result) > 0:
            self.cursor.execute("UPDATE query_results SET count = %s WHERE id = %s",
                                (result[0][-1] + 1, result[0][0]))
        else:
            self.cursor.execute("INSERT INTO query_results (query, count) VALUES (%s, %s)",
                                (self.query, 1))
        self.connection.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
