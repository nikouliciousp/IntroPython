import mysql.connector

# Establish connection to MySQL database
# This script's purpose is to insert data into tables in a test database.
mysql_conn = mysql.connector.connect(
    host="localhost",  # Hostname of the database server (local system)
    user="root",  # Database username
    passwd="",  # Password for the user
    database="testpython",  # Name of the database to connect to
    port=3306  # Port number the MySQL server listens on (default is 3306)
)

# Create a cursor object for executing SQL queries
cursor = mysql_conn.cursor()

# Insert records into the TEACHER table
cursor.execute("INSERT INTO TEACHER (FIRSTNAME, LASTNAME) VALUES (%s, %s)", ("John", "Smith"))
cursor.execute("INSERT INTO TEACHER (FIRSTNAME, LASTNAME) VALUES (%s, %s)", ("Jane", "Doe"))

# Insert records into the STUDENT table
cursor.execute("INSERT INTO STUDENT (FIRSTNAME, LASTNAME, GRADE) VALUES (%s, %s, %s)", ("Alice", "Smith", 95))
cursor.execute("INSERT INTO STUDENT (FIRSTNAME, LASTNAME, GRADE) VALUES (%s, %s, %s)", ("Bob", "Doe", 85))

# Commit the transaction to save changes to the database
mysql_conn.commit()

# Close the cursor and connection
cursor.close()
mysql_conn.close()
