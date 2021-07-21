import logging
import random
import mysql.connector
from mysql.connector.constants import ClientFlag
from dotenv import load_dotenv
import os
import pandas as pd

logger = logging.getLogger()

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
    'database': 'dailyelectroset'
}


# establish connection and initialize cursor
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()  

# read data
data = pd.read_csv("electrosets.csv")

# create a query later to be executed for every row
query = "INSERT IGNORE INTO electrosets (URL, Description) VALUES (%s, %s)"

# for every row (converted to a tuple), execute query
for val in list(data.to_records(index=False)):
    cursor.execute(query, tuple(val))

# commit changes and close connection
cnxn.commit()  
cnxn.close()  