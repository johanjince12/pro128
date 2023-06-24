from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser =  webdriver.Chrome("=")
browser.get(START_URL)

time.sleep(10)

new_planet_data = []

def scrape_more_data(hyperlink):
    try:
        page = requests.get(hyperlink)

        soup = BeautifulSoup(page.content,"html.parser")

        temp_list = []
    
    for tr_tag in soup.find_all("tr",attrs={"class":"fact_row"}):
        td_tags = tr_tag.find_all("td")

        for td_tag in td_tags:
            try:
                temp_list.append(td_tag.find_all("div")