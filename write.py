from connector import ConnectorWrite
import userresult


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


counter = Counter('car')
print(counter.select())
counter.close()

insert_to = InsertTo('car')
insert_to.insert_or_update()
insert_to.close()
