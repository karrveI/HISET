import json
import requests
from bs4 import BeautifulSoup
from config import *

class Scrape:
    def __init__(self) -> None:
        self.url = url
        self.soup = self.get_soup()
        self.json_path = json_path
        self.localdate = self.read_date()
        self.webdate = self.scrape_date()
        
    def get_soup(self): 
        request = requests.get(self.url)
        return  BeautifulSoup(request.content, features="lxml")
        
    def read_date (self) -> str: #read local date from file
        with open("lastUsed.txt", "r") as f:
            return f.read()

    def scrape_date (self) -> str: #scrape date from site
        return self.soup.find("label", attrs={"style": "color:#AC4500;font-size:35px;margin-left:10px;font-family: 'Open Sans Condensed', sans-serif;"}).contents[0]
        
    def get_events(self) -> list:
        data = []
        main = self.soup.find("div", id="content") #main div which contains all events

        event_list = main.find_all("div", class_="row", attrs={"style": "margin-bottom:10px;"}) #get container divs of event info
        data += [{
                "date": event.find("span").contents[0].strip(),
                "title": event.find("a", class_=False).contents[0].strip(),
                "text": event.find("p").contents[0].strip()
                } for event in event_list]
    
        return data
    
    def to_json(self, data) -> None: #save on JSON format to use on ./web
        data = {"events": data}
        with open(self.json_path, "w") as f:
            json.dump(data, f)