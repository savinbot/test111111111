import psycopg2
#import sys

conn_string = "host = 'localhost' dbname = 'db_hw3' user='postgres' password ='ewing' port='5434'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
EnteredP = "AB0000001"
query = "SELECT * FROM student WHERE passport = '" + EnteredP + "' "
print(query)
cursor.execute(query)
records = cursor.fetchall()

print(records) 

men = input("Hello:")
