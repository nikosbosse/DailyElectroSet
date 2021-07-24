import random
from dotenv import load_dotenv
import os
import pandas as pd
import requests as rs
import numpy as np
from bs4 import BeautifulSoup
import requests
from link_preview import link_preview

class randomset: 
    def __init__(self):         
        # URL of google sheet
        self.sheet_url = 'https://docs.google.com/spreadsheets/d/1LNaVwIkU3hucJ707kw_vH5T0Xac6PSWSu14lSjayPto/edit#gid=0'

    def get_random_set(self):
        # get the website using requests
        html = requests.get(self.sheet_url).text

        # parse the website and find all tables
        soup = BeautifulSoup(html, "lxml")
        tables = soup.find_all("table")

        # define output list, than iterate over existing tables (unsure why it finds more than one)
        out = []
        for table in tables:
            # define an empty list that gets then filled with row entries
            l = []
            table_rows = table.find_all('tr')
            for tr in table_rows:
                td = tr.find_all('td')
                row = [tr.text for tr in td]
                l.append(row)
            
            # after iteration has finished, convert to DataFrame and append to output
            df = pd.DataFrame(l)
            out.append(df)

        # put all outputs together (this should merge a filled with an empty DataFrame)
        out = pd.concat(out)

        # get the urls as the first colums and filter out everything that doesn't have https in it
        all_set_urls = out.iloc[:, 0].tolist()
        all_set_urls = [x for x in all_set_urls if "https" in str(x)]

        self.randomseturl = random.choice(all_set_urls)

    def download_title(self): 
        try:
            # get a preview based on the link
            dict_elem = link_preview.generate_dict(self.randomseturl) # this is a dict()

            # Access title and clean formatting
            title = dict_elem['title']
            self.title = title.replace("&amp;", "&")
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
    

    def download_title_image(self, filename):
        try:
            # get a preview based on the link
            dict_elem = link_preview.generate_dict(self.randomseturl) # this is a dict()

            # acces preview image URL and downlaod
            image = dict_elem['image']
            request = requests.get(image)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        with open(filename, "wb") as image:
            image.write(request.content)

    def write_tweet(self):
        message = [
            "Let music brighten your life with a randomly selected high-quality electro set every day!",
            " ",
            f"Today's set is: {self.title}",
            f"{self.randomseturl}",
            " ",
            "Enjoy! \U0001F680 \U0001F31F \U0001F389",
        ]
        message = " \n".join(message)
        return message 
