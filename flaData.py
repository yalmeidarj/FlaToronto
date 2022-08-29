import requests

flamengo_id = "127"
Libertadores = "13"
brasileiraoA = "71"
brasileiraB = "72"
copa_do_Brasil = "73"
brasileiraC = "75"
brasileiraD = "76"
#data = [{'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}]





def fetch_team_matches(season="2022", team="127", from_date=str,to_date=str, next=None, last=None):

	source_url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"

	headers = {
		"X-RapidAPI-Key": "6b3b3ae179msh12092c0b165179fp11063cjsnc52d628c2c4c",
		"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
	}
	if last != None:
		print("working Last")
		querystring = {"team":team, "last":last}
	elif next != None:
		print("working nextt")
		querystring = {"team":team, "next":next}		
	else:
		querystring = {"season":season,"team":team,"from":from_date,"to":to_date}


	data = requests.request("GET", source_url, headers=headers, params=querystring).json()
	match_data = []	


	for match in data["response"]:
		match_dict = {

			"id": match["fixture"]["id"],
			"date": match["fixture"]["date"][:10],
			"time": match["fixture"]["date"][11:16],
			"stadium": match["fixture"]["venue"]["name"],
			"status": match["fixture"]["status"]["short"],
			"city_match": match["fixture"]["venue"]["city"],
			"league": match["league"]["name"],
			"league_logo": match["league"]["logo"],
			"home_team": match["teams"]["home"]["name"],
			"home_team_logo": match["teams"]["home"]["logo"],
			
			"away_team": match["teams"]["away"]["name"],
			"away_team_logo": match["teams"]["away"]["logo"],

			"score":  match["goals"],
			"score_extratime":  match["score"]["extratime"],
			"score_penalty":  match["score"]["penalty"]
		}

		match_data.append(match_dict)

	return match_data

# response_last = fetch_team_matches(last="9")

# response_next = fetch_team_matches(next="9")


response_next = fetch_team_matches(next="3")#[{'id': 838225, 'date': '2022-08-28', 'time': '21:00', 'stadium': 'Estádio Nilton Santos', 'status': 'NS', 'city_match': 'Rio de Janeiro', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Botafogo', 'home_team_logo': 'https://media.api-sports.io/football/teams/120.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 933776, 'date': '2022-09-01', 'time': '00:30', 'stadium': 'Estadio José Amalfitani', 'status': 'NS', 'city_match': 'Capital Federal, Ciudad de Buenos Aires', 'league': 'CONMEBOL Libertadores', 'league_logo': 'https://media.api-sports.io/football/leagues/13.png', 'home_team': 'Velez Sarsfield', 'home_team_logo': 'https://media.api-sports.io/football/teams/438.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838232, 'date': '2022-09-04', 'time': '14:00', 'stadium': 'Estadio Jornalista Mário Filho', 'status': 'NS', 'city_match': 'Rio de Janeiro, Rio de Janeiro', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Flamengo', 'home_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'away_team': 'Ceara', 'away_team_logo': 'https://media.api-sports.io/football/teams/129.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 933777, 'date': '2022-09-08', 'time': '00:30', 'stadium': 'Estadio Jornalista Mário Filho', 'status': 'NS', 'city_match': 'Rio de Janeiro, Rio de Janeiro', 'league': 'CONMEBOL Libertadores', 'league_logo': 'https://media.api-sports.io/football/leagues/13.png', 'home_team': 'Flamengo', 'home_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'away_team': 'Velez Sarsfield', 'away_team_logo': 'https://media.api-sports.io/football/teams/438.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838248, 'date': '202sports.io/football/teams/124.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': '2022-09-28', 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838272, 'date': '2022-10-02', 'time': '00:00', 'stadium': None, 'status': 'TBD', 'city_match': None, 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Flamengo', 'home_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'away_team': 'RB Bragantino', 'away_team_logo': 'https://media.api-sports.io/football/teams/794.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}]

response_last = fetch_team_matches(last="9")

#all_matches = response_last[:1]



# print(response_last[0])













# s = []
# ns = []
# for i in data:
#     if i["status"] == "NS":
#         ns.append(i)
#     else:
#         s.append(i)
# print(f"Started matches: {len(s)}\nNon started matches: {len(ns)}")