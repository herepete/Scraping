#!/usr/bin/python3.7
import requests
import pandas as pd
from bs4 import BeautifulSoup
import os
import time
sleep_time=5
os.system('clear')

# used to decide if i should write out a header on the csv after the first run it will increment to 1
first_run=0


def delete_file():

    file = 'players.csv'
    if(os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
        print("players.csv file deleted")
    else:
        print("players.csv file not found")


def get_data_back(url_to_test,team):
    try:
        header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        r = requests.get(url_to_test, headers=header)
        data=pd.read_html(r.text)

        #conver from list to dataframe
        data=data[0]
        #Only show Active players
        data=data[(data['Status'] == 'ACT')]
        #remove undeeded columns
        data.drop("No",axis='columns',inplace=True)
        data.drop("Status",axis='columns',inplace=True)
        #set a better index
        data=data.set_index("Player")
        #add a new column
        data=data.assign(Team=team)
        #Write to Csv will overwrite anything in place

        if first_run==0:
            #first run 
            #player name at column0 is auto included as it is the index
            #therefore no needed in the below headerList
            headerList=['Position','Height','Weight','Experience','College','Team']
            data.to_csv('players.csv', mode='a',header=headerList)
        else:
            data.to_csv('players.csv', mode='a',header=False)
            #every other run
            
    
        print(f"{team} written to players.csv") 

    except Exception as e:
        print("I failed somewhere")
        print(e)
        breakpoint()


input("About to start Scraping...press enter to continue")
delete_file()

list_of_teams=[["https://www.nfl.com/teams/cleveland-browns/roster","Cleveland Browns"]\
              ,["https://www.nfl.com/teams/arizona-cardinals/roster","Arizona Cardinals"]\
              ,["https://www.nfl.com/teams/baltimore-ravens/roster","Baltimore Ravens"]\
              ,["https://www.nfl.com/teams/atlanta-falcons/roster","Atlanta Falcons"]\
              ,["https://www.nfl.com/teams/buffalo-bills/roster","Buffalo Bills"]\
              ,["https://www.nfl.com/teams/carolina-panthers/roster","Carolina Panthers"]\
              ,["https://www.nfl.com/teams/cincinnati-bengals/roster","Cincinnati Bengals"]\
              ,["https://www.nfl.com/teams/chicago-bears/roster","Chicago Bears"]\
              ,["https://www.nfl.com/teams/dallas-cowboys/roster","Dallas Cowboys"]\
              ,["https://www.nfl.com/teams/denver-broncos/roster","Denver Broncos"]\
              ,["https://www.nfl.com/teams/detroit-lions/roster","Detroit Lions"]\
              ,["https://www.nfl.com/teams/houston-texans/roster","Houston Texans"]\
              ,["https://www.nfl.com/teams/green-bay-packers/roster","Green Bay Packers"]\
              ,["https://www.nfl.com/teams/indianapolis-colts/roster","Indianapolis Colts"]\
              ,["https://www.nfl.com/teams/los-angeles-rams/roster","Los Angeles Rams"]\
              ,["https://www.nfl.com/teams/jacksonville-jaguars/roster","Jacksonville Jaguars"]\
              ,["https://www.nfl.com/teams/minnesota-vikings/roster","Minnesota Vikings"]\
              ,["https://www.nfl.com/teams/kansas-city-chiefs/roster","Kansas City Chiefs"]\
              ,["https://www.nfl.com/teams/new-orleans-saints/roster","New Orleans Saints"]\
              ,["https://www.nfl.com/teams/las-vegas-raiders/roster","Las Vegas Raiders"]\
              ,["https://www.nfl.com/teams/new-york-giants/roster","New York Giants"]\
              ,["https://www.nfl.com/teams/los-angeles-chargers/roster","Los Angeles Chargers"]\
              ,["https://www.nfl.com/teams/philadelphia-eagles/roster","Philadelphia Eagles"]\
              ,["https://www.nfl.com/teams/miami-dolphins/roster","Miami Dolphins"]\
              ,["https://www.nfl.com/teams/san-francisco-49ers/roster","San Francisco 49ers"]\
              ,["https://www.nfl.com/teams/new-england-patriots/roster","New England Patriots"]\
              ,["https://www.nfl.com/teams/seattle-seahawks/roster","Seattle Seahawks"]\
              ,["https://www.nfl.com/teams/new-york-jets/roster","New York Jets"]\
              ,["https://www.nfl.com/teams/tampa-bay-buccaneers/roster","Tampa Bay Buccaneers"]\
              ,["https://www.nfl.com/teams/pittsburgh-steelers/roster","Pittsburgh Steelers"]\
              ,["https://www.nfl.com/teams/washington-commanders/roster","Washington Commanders"]\
              ,["https://www.nfl.com/teams/tennessee-titans/roster","Tennessee Titans"]\
              ]  

for i in list_of_teams:
    get_data_back(url_to_test=i[0],team=i[1])
    print(f"Having a {sleep_time} Sleep...to reduce unfairley bombrading servers")
    time.sleep(sleep_time)
    

#get_data_back(url_to_test="https://www.nfl.com/teams/cleveland-browns/roster",team="Cleveland Browns")
#time.sleep(sleep_time)
#get_data_back(url_to_test="https://www.nfl.com/teams/arizona-cardinals/roster",team="Arizona Cardinals")
    
