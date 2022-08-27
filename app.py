from flask import Flask, flash, render_template, request, redirect, url_for
import config
import requests
import flaData

response_next = flaData.response_next
response_last = flaData.response_last

print(response_last[0])




data = [{'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}]




def page_not_found(e):
  return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])



@app.route('/', methods = ["GET", "POST"])
def index():

   league_next = response_next[0]["league"]
   home_team_next = response_next[0]["home_team"]
   away_team_next = response_next[0]["away_team"]
   home_team_logo_next = response_next[0]["home_team_logo"]
   away_team_logo_next = response_next[0]["away_team_logo"]

   all_matches = response_last[1:9]
   league_last = response_last[0]["league"]
   match_date_last = response_last[0]["date"]
   match_time_last = response_last[0]["time"]
   score_home_last = response_last[0]["score"]["home"]
   score_away_last = response_last[0]["score"]["away"]
   home_team_last = response_last[0]["home_team"]
   away_team_last = response_last[0]["away_team"]
   home_team_logo_last = response_last[0]["home_team_logo"]
   away_team_logo_last = response_last[0]["away_team_logo"]
   return render_template('index.html', **locals())

@app.route('/i', methods = ["GET", "POST"])
def i():

   return render_template('i.html', **locals())


@app.route('/login', methods = ["GET", "POST"])
def login():

   return render_template('login.html', **locals())

@app.route('/register', methods = ["GET", "POST"])
def register():

   return render_template('register.html', **locals())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8888', debug=True)