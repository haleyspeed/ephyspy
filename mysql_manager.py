import mysql.connector
from mysql.connector import errorcode

def printstuff():
    print("woohoo")

def create_database(cursor, DB_NMAE):
    try:
        cursor.execute(
            "CREATE DATABASE: {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Create database failed {}:".format(err))
        exit(1)

# Change to the database indicated by DB_NAME
def locate_database(cursor, DB_NAME):
    try:
        cursor.execute("USE {}".format(DB_NAME))
        print("Data base {}".format(DB_NAME), " is alive.")
    except mysql.connector.Error as err:
        print("Database {} does note exist.".format(DB_NAME))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            mysql_manager.create_database(cursor, DB_NMAE)
            print("Database {} created successfully.".format(DB_NAME))
            cnx.database = DB_NAME
        else:
            print(err)
            exit(1)

# Iterate through the existing tables and check to see if the desired table already exists
# If not, it creates the database
def create_table (cursor, table_name):
    table_description = table_name
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")