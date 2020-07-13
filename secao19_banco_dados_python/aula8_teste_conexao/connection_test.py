#! python

from database.new_connection_function import new_connection

with new_connection() as connection:
    if connection.is_connected():
        print('Connected')
print('Connection terminated')
