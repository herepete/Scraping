#!/usr/bin/python3.7
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
os.system('clear')

print("This script will you understand about how to Scrape the data of a webpage")
user_input=input("Please enter a site to check i.e (https://bbc.co.uk)")
if user_input =="":
    print ("Because nothing has been entered i am going to use a pre-defined URL for testing")
    url="https://www.espn.com/nfl/team/roster/_/name/phi/philadelphia-eagles"
else:
    url=user_input
print (f"SITE TO CHECK -{url}")


def fake_browser_attempt(url_to_test):
    try:
        #url="https://www.espn.com/nfl/team/roster/_/name/phi/philadelphia-eagles"
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        r = requests.get(url, headers=header)
        data=pd.read_html(r.text)
        #data=pd.read_html(r.text)
        print ("Fake Browser option worked")
        print(data[0].head())
    except:
        print ("Fake Browser option failed...")

def basic_html_table(url_to_test):
    #largely taken from https://www.scrapingbee.com/blog/python-web-scraping-beautiful-soup/
    #response = requests.get("https://news.ycombinator.com/")
    response = requests.get(url_to_test)
    if response.status_code != 200:
        print("Error fetching page")
        exit()
    else:
        content = response.content
    input("About to print content")
    print(content)
 
    soup = BeautifulSoup(response.content, 'html.parser')
 
    # The title tag of the page
    input("About to print page title")
    print(soup.title)
 
    # The title of the page as string
    input("About to print page title as string")
    print(soup.title.string)
 
    # All links in the page
    input("About to print all links")
    nb_links = len(soup.find_all('a'))
    print(f"There are {nb_links} links in this page")
 
    # Text from the page
    print(soup.get_text())

    input("About to print pretty print...")
    print(soup.prettify())


input("About to do fake browser test...")
fake_browser_attempt(url_to_test=url)
input("About to dobasic html test")
basic_html_table(url_to_test=url)
