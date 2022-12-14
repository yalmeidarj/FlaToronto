from flask import Flask, flash, render_template, request, redirect, url_for, current_app, send_file, abort
import config as config
import requests
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from sqlalchemy.engine import result
import sqlalchemy
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
import data_manager as dm
from werkzeug.utils import secure_filename
import imghdr
import vidhdr



data_manager = dm.DataManager()

# data_manager.insert_into_table(table="user", match_info=(None, "User", "Irssy", "PErdda", "iuypedrsaa@gmail.com", "dkjfaldkjfalkdjf"), cols="(id, permissions, name, username, email, pwd)")


# def page_not_found(e):
#   return render_template('404.html'), 404

def create_app():    
    app = Flask(__name__)
    app.config.from_object(config.config['development'])
    app.config['SQLALCHEMY_DATABASE_URI'] =  "sqlite:///fla.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    return app
app = create_app()

engine = create_engine("sqlite:///fla.db")
 
# initialize the Metadata Object
meta = MetaData(bind=engine)
MetaData.reflect(meta)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader

## TABLE
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permissions = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(250), nullable=False)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True,nullable=False)
    phone = db.Column(db.String(250), unique=True)
    CPF = db.Column(db.String(250), unique=True)
    pwd = db.Column(db.String(750), nullable=False)


    def get_id(self):
           return (self.id)

    def __repr__(self):
        return f'<User {self.name}>'
    

## TABLE
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(250))
    time = db.Column(db.String(250))
    stadium = db.Column(db.String(250))
    status = db.Column(db.String(250))
    city_match = db.Column(db.String(250))
    league = db.Column(db.String(250))
    league_logo = db.Column(db.String(750))
    home_team = db.Column(db.String(250))
    home_team_id = db.Column(db.String(250) )
    home_team_logo = db.Column(db.String(250))
    away_team = db.Column(db.String(250)) 
    away_team_id = db.Column(db.String(250) )
    away_team_logo = db.Column(db.String(250))
    score = db.Column(db.String(250))
    score_extratime = db.Column(db.String(250))
    score_penalty = db.Column(db.String(750))
    match_id = db.Column(db.Integer)

    #Optional: this will allow each Match object to be identified by its title when printed.
    def __repr__(self):
        return f'<Match {self.id}>'


def load_user(id):
    return User.query.get(id)
## Db query
response_next = db.session.query(Match).filter(Match.status == "NS").group_by(Match.date).all()
response_last = db.session.query(Match).filter(Match.status == "FT").group_by(Match.date).all()[::-1]


@app.route('/', methods = ["GET", "POST"])
def index():

   league_next = response_next[0].league
   next_match_date = response_next[0].date
   next_match_time = response_next[0].time
   match_next_datetime = f"{next_match_date} {next_match_time}".replace("-", "/" )
   home_team_next = response_next[0].home_team
   away_team_next = response_next[0].away_team
   home_team_logo_next = response_next[0].home_team_logo
   away_team_logo_next = response_next[0].away_team_logo

   all_matches = response_last
   league_last = response_last[0].league

   match_date_last = response_last[0].date
   match_time_last = response_last[0].time
   score_home_last = response_last[0].score[0]
   score_away_last = response_last[0].score[4]
   home_team_last = response_last[0].home_team
   away_team_last = response_last[0].away_team
   home_team_logo_last = response_last[0].home_team_logo
   away_team_logo_last = response_last[0].away_team_logo
   return render_template('index.html', **locals())


@app.route('/registrar' , methods = ['GET','POST'])
def registrar():  
  if request.method =='POST':
    error = None 
    userName = request.form.get("username") 
    userName = db.session.query(User).filter_by(username=userName).first()
    if userName:      
      flash('Email j?? registrado. Use outro Email ou entre em sua conta.')
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
         db.session.add(User(
            permissions="User", name=name, username=username, email=email, CPF=None, phone=None,  pwd=password_hash
            ))
         db.session.commit()
         flash('Pedido de registro de conta efetivado. Por favor, aguarde at?? que a Administra????o aprove seu registro antes de entrar em sua conta.')
         return redirect(url_for('registrar'))
        except:
         
         flash("Usu??rio n??o dispon??vel. Tente um Nome de Usu??rio diferente")
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
         flash('Credenciais n??o autorizadas. Tente novamente ou entre em contato com o Administrador')
         return redirect(url_for('login'))
   elif email:
      if check_password_hash(email.pwd, password):
         #login_user(email, remember=True)
         return redirect(url_for('index'))        
      else:
         flash('Credenciais n??o autorizadas. Tente novamente ou entre em contato com o Administrador')
         return redirect(url_for('login'))
   else:
      flash('Usu??rio n??o existente. Tente novamente ou entre em contato com o Administrador')

  return render_template('login.html', **locals())




@app.route('/about', methods = ["GET", "POST"])
def about():

   return render_template('about.html', **locals())

@app.route('/gallery', methods = ["GET", "POST"])
def gallery():

   return render_template('gallery.html', **locals())

@login_required
@app.route('/g', methods = ["GET", "POST"])
def g():

   return render_template('g.html', **locals())


@app.route('/matches', methods = ["GET", "POST"])
def matches():
   league_next = response_next[0].league
   next_match_date = response_next[0].date
   next_match_time = response_next[0].time
   match_next_datetime = f"{next_match_date} {next_match_time}".replace("-", "/" )
   home_team_next = response_next[0].home_team
   away_team_next = response_next[0].away_team
   home_team_logo_next = response_next[0].home_team_logo
   away_team_logo_next = response_next[0].away_team_logo

   all_matches = response_last
   league_last = response_last[0].league

   match_date_last = response_last[0].date
   match_time_last = response_last[0].time
   score_home_last = response_last[0].score[0]
   score_away_last = response_last[0].score[4]
   home_team_last = response_last[0].home_team
   away_team_last = response_last[0].away_team
   home_team_logo_last = response_last[0].home_team_logo
   away_team_logo_last = response_last[0].away_team_logo

   return render_template('matches.html', **locals())

@app.route('/team', methods = ["GET", "POST"])
def team():

   return render_template('team.html', **locals())

@app.route('/contact', methods = ["GET", "POST"])
def contact():

   return render_template('contact.html', **locals())


app.config['MAX_CONTENT_LENGTH'] = 2040 * 2040
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.mp4']
app.config['UPLOAD_PATH'] = "c:/Users/yalme/Downloads/sportz-gh-pages/sportz-gh-pages/static/images/uploads"


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

def validate_video(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = vidhdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'mp5' else 'mp4')

@app.route('/media')
def media():
    return render_template('media.html')


@app.route('/media', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext == ".mp4":
            print(file_ext)
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        elif file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)
      #   elif file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
      #           file_ext != validate_video(uploaded_file.stream):
      #       abort(400)            
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return redirect(url_for('media'))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port='8888', debug=True)