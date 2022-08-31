from msilib.schema import Error
import requests
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv("c:/Users/yalme/Downloads/sportz-gh-pages/sportz-gh-pages/pwd.txt")

a = os.environ.get("X-RapidAPI-Key")
b = os.environ.get("X-RapidAPI-Host") 


# flamengo_id = "127"
# Libertadores = "13"
# brasileiraoA = "71"
# brasileiraB = "72"
# copa_do_Brasil = "73"
# brasileiraC = "75"
# brasileiraD = "76"


database = r"C:\Users\yalme\Downloads\sportz-gh-pages\sportz-gh-pages\fla.db"
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    """

    conn = None
    conn = sqlite3.connect(db_file)


    return conn

def insert_into_table(table, match_info, cols=None ):
    '''Create database connection;
    Insert data to table in database.
    match_info --> takes match values;
    cols --> takes the columns names of table. Default to None. If None, Match cols are needed    
    '''
    
    conn = create_connection(database)

    if cols != None:
        sql = f''' INSERT INTO {table}({cols})
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) ''' 
    else:
        sql = f''' INSERT INTO {table}( 
        id, date, time,
        stadium, status, city_match,
        league, league_logo, home_team,
        home_team_id, home_team_logo, away_team,
        away_team_id, away_team_logo, score,
        score_extratime, score_penalty)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)  '''

    cur = conn.cursor()
    cur.execute(sql, match_info)
    conn.commit()
    conn.close()

    return cur.lastrowid


def fetch_matches(season="2022", team="127", from_date=str,to_date=str, next=None, last=None):
    '''# Pulls match data from Football API
    Takes only one of 3 parameters (string):
        last or next (number of matches to fetch eg next='3'), or from_date/to_date 
    Team Id default to "Flamengo", "127".'''
    
    source_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

    headers = {
        "X-RapidAPI-Key": os.environ.get("X-RapidAPI-Key"), 
        "X-RapidAPI-Host": os.environ.get("X-RapidAPI-Host")
    }
    
    if last != None:
        querystring = {"team":team, "last":last}
    elif next != None:
        querystring = {"team":team, "next":next}		
    else:
        querystring = {"season":season,"team":team,"from":from_date,"to":to_date}

    data = requests.request("GET", source_url, headers=headers, params=querystring).json()
    return data["response"]


def insert_match_to_db(func:list):
    '''# Takes function output (list) and feeds databse'''

    def convert_to_tuple(list_data:list):    
        return tuple(list_data)
         
    
    matches = func
    

    for match in matches:
        
        id = int(match["fixture"]["id"])
        date = match["fixture"]["date"][:10]        
        time = match["fixture"]["date"][11:16]        
        stadium = match["fixture"]["venue"]["name"]        
        status = match["fixture"]["status"]["short"]        
        city_match = match["fixture"]["venue"]["city"]        
        league = match["league"]["name"]        
        league_logo = match["league"]["logo"]        
        home_team = match["teams"]["home"]["name"]        
        home_team_id = str(match["teams"]["home"]["id"])        
        home_team_logo = match["teams"]["home"]["logo"]        
        away_team = match["teams"]["away"]["name"]        
        away_team_id = str(match["teams"]["away"]["id"])        
        away_team_logo = match["teams"]["away"]["logo"]        
        score =  f'{match["goals"]["home"]} : {match["goals"]["away"]}'        
        score_extratime =  f'{match["score"]["extratime"]["home"]} : {match["score"]["extratime"]["away"]}'        
        score_penalty = f'{match["score"]["penalty"]["home"]} : {match["score"]["penalty"]["away"]}'
        
        match_data=[
            id, date, time, stadium, status, city_match,
            league, league_logo, home_team, home_team_id,
            home_team_logo, away_team, away_team_id, away_team_logo, score,
            score_extratime, score_penalty
        ]

        values = convert_to_tuple(match_data) 
        insert_into_table("Match", values)


# insert_match_to_db(fetch_matches(next="3"))
# insert_match_to_db(fetch_matches(last="9"))
