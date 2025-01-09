import mysql.connector

# Establishing the connection to MySQL server
mysql_conn = mysql.connector.connect(
    host="localhost",  # Host where the database server is running
    user="root",  # Username for the database
    passwd="",  # Password for the user
)

# Initializing a cursor object to interact with the MySQL server
cursor = mysql_conn.cursor()

# Executing a SQL query to create a new database named 'testpython'
cursor.execute("CREATE DATABASE IF NOT EXISTS testpython")

# Close the cursor and connection
cursor.close()
mysql_conn.close()
