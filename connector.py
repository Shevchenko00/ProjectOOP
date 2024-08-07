import mysql.connector


class ConnectorRead:
    def __init__(self, config):
        print("Opening connection...")
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        print("Connection established")

    def __del__(self):
        self.close_connection()

    def close_connection(self):
        if self.cursor:
            print("Closing cursor...")
            self.cursor.close()
        if self.connection:
            print("Closing connection...")
            self.connection.close()
        print("Connection closed")

    @staticmethod
    def get_connect(database="sakila"):
        dbconfig = {
            
        }
        return mysql.connector.connect(**dbconfig)


class ConnectorWrite:
    def __init__(self, config):
        print("Opening connection...")
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        print("Connection established")

    def find_by_str(self, user_query):
        self.cursor.execute("SELECT * FROM 310524ptm_O_Shevchenko.query_results WHERE query = %s;",
                            (user_query,))
        return self.cursor.fetchall()

    def __del__(self):
        self.close_connection()

    def close_connection(self):
        if self.cursor:
            print("Closing cursor...")
            self.cursor.close()
        if self.connection:
            print("Closing connection...")
            self.connection.close()
        print("Connection closed")

    @staticmethod
    def get_connect(database="310524ptm_O_Shevchenko"):
        dbconfig = {
            
        return mysql.connector.connect(**dbconfig)
