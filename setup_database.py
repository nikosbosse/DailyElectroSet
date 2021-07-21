# this is only run once to set everything up!
import mysql.connector
from mysql.connector.constants import ClientFlag
from dotenv import load_dotenv
import os

# load password for database
load_dotenv()
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

config = {
    'user': 'root',
    'password': MYSQL_PASSWORD,
    'host': '104.198.24.234',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem',
}

# establish connection and create database
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()  # initialize connection cursor
cursor.execute('CREATE DATABASE dailyelectroset')
cnxn.close()  # close connection because we will be reconnecting to dailyelectro data base

config['database'] = 'dailyelectroset'  # add new database to config dict



# establish connection to database and create new table
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()  # initialize connection cursor
cursor.execute("CREATE TABLE electrosets ("
               "URL VARCHAR(512) PRIMARY KEY,"
               "Description VARCHAR(512) )")


cnxn.commit()  # this commits changes to the database
cnxn.close()  # close connection because we will be reconnecting to testdb
