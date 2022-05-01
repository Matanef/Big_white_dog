import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Doobi123'
DATABASE = 'Exercise_XP_28-04'

class MenuItem:
    def __init__ (self, item_name_menu, item_price_menu):
        self.item_name_menu = item_name_menu
        self.item_price_menu = item_price_menu
    



    def save(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(f'''INSERT INTO items(item_name, item_price) VALUES('{self.item_name_menu}', {self.item_price_menu} RETURNING id, item_name_menu, item_price_menu)''')
        connection.commit()
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()





    def delete(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM restmenu WHERE item_name = '{self.item_name_menu}'")
        connection.commit()
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()





    def update(self, item_name_menu, item_price_menu):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(f'UPDATE items SET item_name = '{self.item_name_menu}', item_price = '{self.item_price_menu}')')
        connection.commit()
        self.item_name_menu = item_name_menu
        self.item_price_menu = item_price_menu
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()


    @classmethod
    def all(cls):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * from restmenu')
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()


    @classmethod
    def get_by_name(cls, name):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(f'SELECT * from restmenu')
        try:
            results = cursor.fetchall()
            connection.close()
            return results
        except:
            connection.close()
