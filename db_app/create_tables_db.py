import mysql.connector

# Establish connection to MySQL database
# This script's purpose is to set up tables in a test database.
mysql_conn = mysql.connector.connect(
    host="localhost",  # Hostname of the database server (local system)
    user="root",  # Database username
    passwd="",  # Password for the user
    database="testpython",  # Name of the database to connect to
    port=3306  # Port number the MySQL server listens on (default is 3306)
)

# Create a cursor object for executing SQL queries
cursor = mysql_conn.cursor()

# Begin a transaction
# Transactions ensure database operations occur as a single unit of work,
# maintaining data consistency and integrity.
cursor.execute("START TRANSACTION")

# Create TEACHER table with columns for ID, FIRSTNAME, and LASTNAME
cursor.execute('''CREATE TABLE IF NOT EXISTS TEACHER (
    ID INT PRIMARY KEY AUTO_INCREMENT,  -- Auto incrementing primary key
    FIRSTNAME VARCHAR(50) NOT NULL,     -- First name of the teacher
    LASTNAME VARCHAR(50) NOT NULL       -- Last name of the teacher
)''')

# Create STUDENT table with columns for ID, FIRSTNAME, LASTNAME, and GRADE
cursor.execute('''CREATE TABLE IF NOT EXISTS STUDENT (
    ID INT PRIMARY KEY AUTO_INCREMENT,  -- Auto incrementing primary key
    FIRSTNAME VARCHAR(50) NOT NULL,     -- First name of the student
    LASTNAME VARCHAR(50) NOT NULL,      -- Last name of the student
    GRADE INT                           -- Grade of the student
)''')

# Commit the transaction to save changes to the database
mysql_conn.commit()

# Close the cursor and connection
cursor.close()
mysql_conn.close()
