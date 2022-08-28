from flask import Flask, flash, render_template, request, redirect, url_for
import config
import requests
import flaData
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from sqlalchemy.engine import result
import sqlalchemy

response_next = flaData.response_next
response_last = flaData.response_last



data = [{'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}, {'id': 838267, 'date': ('2022-09-28',), 'time': '22:00', 'stadium': 'Estádio Governador Plácido Aderaldo Castelo', 'status': 'NS', 'city_match': 'Fortaleza, Ceará', 'league': 'Serie A', 'league_logo': 'https://media.api-sports.io/football/leagues/71.png', 'home_team': 'Fortaleza EC', 'home_team_logo': 'https://media.api-sports.io/football/teams/154.png', 'away_team': 'Flamengo', 'away_team_logo': 'https://media.api-sports.io/football/teams/127.png', 'score': {'home': None, 'away': None}, 'score_extratime': {'home': None, 'away': None}, 'score_penalty': {'home': None, 'away': None}}]




# def page_not_found(e):
#   return render_template('404.html'), 404

app = Flask(__name__)
app.config.from_object(config.config['development'])


app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///fla.db"# "postgresql://hostman:4e12f875@143.198.52.41:5433/database"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##CREATE TABLE
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True,nullable=False)
    phone = db.Column(db.String(250), unique=True)
    CPF = db.Column(db.String(250), unique=True)
    pwd = db.Column(db.String(750), nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<User {self.name}>'
    





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

# @app.route('/i', methods = ["GET", "POST"])
# def i():

#    return render_template('i.html', **locals())

@app.route('/registrar' , methods = ['GET','POST'])
def registrar():  
  if request.method =='POST':
    error = None 
    userName = request.form.get("username") 
    userName = db.session.query(User).filter_by(username=userName).first()
    if userName:      
      flash('Email já registrado. Use outro Email ou entre em sua conta.')
      # Account already exists.

    else:
      name = request.form.get("name")
      username = request.form.get("username")
      email = request.form.get("email")
      password = request.form.get("password")
      password_confirm = request.form.get("password_confirm")
      if password == password_confirm:

        # password confirmed
        password_hash = generate_password_hash(password, method='sha256')
        try:

         db.session.add(User(permissions="User", name=name, username=username, email=email, CPF=None, phone=None,  pwd=password_hash))
         db.session.commit()
         flash('Pedido de registro de conta efetivado. Por favor, aguarde até que a Administração aprove seu registro antes de entrar em sua conta.')
         return redirect(url_for('registrar'))
        except:
         
         flash("Tente novamente com Nome de Usuário diferente")
         return redirect(url_for('registrar'))

      else:
        flash('Senha divergente. Por favor, verique sua senha e repita a MESMA senha para o cadastro.')
        return redirect(url_for('registrar'))

  return render_template('register.html', **locals())




@app.route('/login', methods = ['GET','POST'])
def login():
  error = None
  if request.method =='POST':

   username = request.form.get("email")
   password = request.form.get("password")
   user = db.session.query(User).filter_by(username=username).first()
   email = db.session.query(User).filter_by(email=username).first()
   if user:
      if check_password_hash(user.pwd, password):
         #login_user(user, remember=True)
         return redirect(url_for('index'))
      else:
         flash('Credenciais não autorizadas. Tente novamente ou entre em contato com o Administrador')
         return redirect(url_for('login'))
   elif email:
      if check_password_hash(email.pwd, password):
         #login_user(email, remember=True)
         return redirect(url_for('index'))        
      else:
         flash('Credenciais não autorizadas. Tente novamente ou entre em contato com o Administrador')
         return redirect(url_for('login'))
   else:
      flash('Usuário não existente. Tente novamente ou entre em contato com o Administrador')

  return render_template('login.html', **locals())




@app.route('/about', methods = ["GET", "POST"])
def about():

   return render_template('about.html', **locals())

@app.route('/gallery', methods = ["GET", "POST"])
def gallery():

   return render_template('gallery.html', **locals())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8888', debug=True)