import psycopg2

# HOSTNAME = 'localhost'
# USERNAME = 'postgres'
# PASSWORD = 'Doobi123'
# DATABASE = 'users'

# def run_query(query):
#     connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
# # cursor 
#     cursor = connection.cursor()

# # execute query
#     cursor.execute(query)
#     connection.commit()
#     results = cursor.fetchall()
#     connection.close()
#     return results
# # for item in results:
# #         print(item)



# def create_table_query(name, **kwargs):
#     q= f'Create table {name} ('
#     for field_name, field_type in kwargs.items():
#         q+= f'{field_name} { field_type},'
#     return q[:-1] + ')'

# # print(create_table_query('user_passwords', id= 'serial primary key', user_name= 'varchar(100)' ))

# # run_query(q)

# def add_user_query(user_name, user_password):
#     q = f"INSERT INTO user_password (user_name, user_password) VALUES ('{user_name}', '{user_password}') RETURNING id, user_name, user_password;"
#     return run_query(q)

# new_user = add_user_query('Matan', '1234')

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Doobi123'
DATABASE = 'users'


def run_query(query):
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    try:
        results = cursor.fetchall()
        connection.close()
        return results
    except:
        connection.close()
    
def create_table_query(name, **kwargs):
    q = f'Create table {name} ('
    for field_name, field_type in kwargs.items():
        q += f'{field_name} {field_type},'
    return q[:-1] + ')'
# print(create_table_query('matan'))

def add_user_query(user_name, password):
    q = f"INSERT INTO user_passwords (user_name, user_password) VALUES '{user_name}', '{password}' RETURNING id, user_name, user_password;"
    return run_query(q)

somevar = create_table_query('Register', id = 'serial primary key', user_name = 'varchar(100)', password = 'varchar(20)')
# print(somevar)
run_query(somevar)

