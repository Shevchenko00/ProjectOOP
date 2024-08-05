from connector import ConnectorRead


# connection = ConnectorRead.get_connect()
# cursor = connection.cursor()
# cursor.execute("SELECT * FROM sakila.actor;")
# result = cursor.fetchall()
# print(result)
# cursor.close()
# connection.close()


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
        select =  f"""select distinct
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
where title like '%{self.query}%' or 
description like '%{self.query}%' or 
release_year like '%{self.query}%' or
first_name like '%{self.query}%' or
name like '%{self.query}%' limit 5000;
"""
        self.cursor.execute(select)
        self.data = self.cursor.fetchall()
        self.result_print()


search = Search('car')
print(search.get_result_search())
