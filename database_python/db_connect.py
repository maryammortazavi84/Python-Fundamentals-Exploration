import psycopg2

input = input('id = ')

conn = psycopg2.connect(database = 'dvdrental', host = 'localhost', user = 'postgres',password = 'mary13841384', port = 5432)

cursor = conn.cursor()

sql_query = f'select * from customer where customer_id = %s;'
cursor.execute(sql_query, (input, ))

print(cursor.fetchone())
print(cursor.fetchmany(size= 10))
print(cursor.fetchall())
