import random
import mysql.connector
from mysql.connector.constants import ClientFlag
from dotenv import load_dotenv
import os
import pandas as pd

class randomset: 
    def __init__(self): 
        # load stored password
        load_dotenv()
        MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

        # database config
        self.config = {
            'user': 'root',
            'password': MYSQL_PASSWORD,
            'host': '104.198.24.234',
            'client_flags': [ClientFlag.SSL],
            'ssl_ca': 'server-ca.pem',
            'ssl_cert': 'client-cert.pem',
            'ssl_key': 'client-key.pem',
            'database': 'dailyelectroset'
        }

    def get_random_set(self):
        # establish connection and initialize cursor
        cnxn = mysql.connector.connect(**self.config)
        cursor = cnxn.cursor()

        # read data from database
        query = "SELECT URL, Description FROM electrosets"
        cursor.execute(query)
        allsets = pd.DataFrame(cursor.fetchall())

        column_names = [i[0] for i in cursor.description]
        allsets.columns = column_names

        # select a random set from all sets
        all_set_urls = allsets['URL']
        self.randomseturl = random.choice(all_set_urls)

        # close connection
        cnxn.close()  

    def write_tweet(self):
        message = [
            "Let music brighten your life with a randomly selected high-quality electro set every day!",
            " ",
            "Enjoy! \U0001F680 \U0001F31F \U0001F389",
            f"{self.randomseturl}"
        ]
        message = " \n".join(message)
        return message 