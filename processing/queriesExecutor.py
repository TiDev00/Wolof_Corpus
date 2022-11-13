import mysql.connector

configs = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
    'database': 'bible',
    'raise_on_warnings': True
}


conn = mysql.connector.connect(**configs)

cursor = conn.cursor(dictionary=True)



conn.close()
