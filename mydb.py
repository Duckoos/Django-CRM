import mysql.connector
import pymysql
#using pymysql library and changed the authentication plugin to native_password (authentication method for older sql versions) from
#caching_sha2_password (new authentication method for newer versions) because for some reason mysql.connector library was not compatible with the newer version of sql even after updating and upgrading it.

#creating a database connection
dataBase = pymysql.connect(
    host = 'localhost', 
    user = 'root',
    passwd = '12345',
    )

# Prepare a cursor object
# It is an object that is used to make the connection for executing SQL queries.
cursorObject = dataBase.cursor()

#create the database
#"CREATE DATABASE my_database_name" is indeed a string inside "" when written in your Python code.
# However, when you pass this string to the cursorObject.execute() method, it is sent to the database server as an SQL command.
cursorObject.execute("CREATE DATABASE nicaco")

print("All Done")