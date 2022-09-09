from msilib.schema import Error
import requests
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv("c:/Users/yalme/Downloads/sportz-gh-pages/sportz-gh-pages/pwd.txt")

a = os.environ.get("X-RapidAPI-Key")
b = os.environ.get("X-RapidAPI-Host") 

# pedro = "10321"
# flamengo_id = "127"
# Libertadores = "13"
# brasileiraoA = "71"
# brasileiraB = "72"
# copa_do_Brasil = "73"
# brasileiraC = "75"
# brasileiraD = "76"


database = r"C:\Users\yalme\Downloads\sportz-gh-pages\sportz-gh-pages\fla.db"

class DataManager:
    def __init__(self) -> None:        
        pass

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        """

        conn = None
        conn = sqlite3.connect(db_file)


        return conn

    def insert_into_table(self, table, match_info, cols=None, db=database ):
        '''Create database connection based on db param; db default with database variable
        Insert data to table in database.
        match_info: Tuple with string ("items", "items") --> takes match values;
        cols: String with tuple "(items, items)" --> takes the columns names of table. Default to None. If None, Match cols are needed    
        '''
        
        conn = self.create_connection(db)

        if cols != None:            
            values_lenght = (len(str(cols).split(", ")) * "?,")[:-1]
            sql = f''' INSERT INTO {table}{cols}
            VALUES({values_lenght}) ''' 
        else:
            sql = f''' INSERT INTO {table}( 
            id, date, time,
            stadium, status, city_match,
            league, league_logo, home_team,
            home_team_id, home_team_logo, away_team,
            away_team_id, away_team_logo, score,
            score_extratime, score_penalty, match_id)
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)  '''

        cur = conn.cursor()
        cur.execute(sql, match_info)
        conn.commit()
        conn.close()

        return cur.lastrowid


    def fetch_matches(self,season="2022", team="127", from_date=str,to_date=str, next=None, last=None):
        '''Pulls match data from Football API
        Takes only one of 3 parameters (string):
            last or next (number of matches to fetch eg next='3'), or from_date/to_date 
        Team Id default "127"(Flamengo). Season default to "2022"'''
        
        source_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

        headers = {
            "X-RapidAPI-Key": os.environ.get("X-RapidAPI-Key"), 
            "X-RapidAPI-Host": os.environ.get("X-RapidAPI-Host")
        }
        
        if last != None:
            querystring = {"team":team, "last":last, "timezone": "America/Toronto"}
        elif next != None:
            querystring = {"team":team, "next":next, "timezone": "America/Toronto"}		
        else:
            querystring = {"season":season,"team":team,"from":from_date,"to":to_date, "timezone": "America/Toronto"}

        data = requests.request("GET", source_url, headers=headers, params=querystring).json()
        return data["response"]


    def insert_match_to_db(self, func:list):
        '''# Takes function output (list) and feeds databse'''

        def convert_to_tuple(list_data:list):    
            return tuple(list_data)
            
        
        matches = func
        
        for match in matches:
            
            id = None
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
            match_id = int(match["fixture"]["id"])
            match_data=[
                id, date, time, stadium, status, city_match,
                league, league_logo, home_team, home_team_id,
                home_team_logo, away_team, away_team_id, away_team_logo, score,
                score_extratime, score_penalty, match_id
            ]

            values = convert_to_tuple(match_data) 
            self.insert_into_table("Match", values)


    def update_db(self):
        '''Create database connection;
        Delets all data from database.
        Fetch next 3 and last 9 matches from Football Api.
        Inserts new data into database   
        '''    
        conn = self.create_connection(database)
        sql = f'''DELETE 
        FROM match
        WHERE id < 13'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        conn.close()
        self.insert_match_to_db(self.fetch_matches(next="3"))
        self.insert_match_to_db(self.fetch_matches(last="9"))

a = DataManager()
a.update_db()
