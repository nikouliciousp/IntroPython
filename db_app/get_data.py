import mysql.connector

# Establish connection to MySQL database
mysql_conn = mysql.connector.connect(
    host="localhost",  # Hostname of the database server (local system)
    user="root",  # Database username
    passwd="",  # Password for the user
    database="testpython",  # Name of the database to connect to
    port=3306  # Port number the MySQL server listens on (default is 3306)
)

# Create a cursor object for executing SQL queries
cursor = mysql_conn.cursor()

# Execute SQL query to retrieve all rows from the TEACHER table
cursor.execute("SELECT * FROM TEACHER")

# Loop through the results and print each row with formatted output
try:
    for row in cursor:
        print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}")
except Exception as e:
    print(f"An error occurred: {e}")

print(f"\n{'-' * 60}\n")

# Execute SQL query to retrieve all rows from the STUDENT table
cursor.execute("SELECT * FROM STUDENT")

# Loop through the results and print each row with formatted output
for row in cursor:
    print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Grade: {row[3]}")

# Close the cursor and connection
cursor.close()
mysql_conn.close()
