import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_dance.consumer import OAuth2ConsumerBlueprint
from dotenv import load_dotenv
load_dotenv() #Load environmental variables


#############################################
############FOR DEVELOPMENT ONLY#############
#############################################

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = '1'
os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = '1'

#############################################

login_manager = LoginManager()

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py') #instance config i.e. secrets


#############################################
################CONFIG FILES#################
#############################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

#############################################

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = "auth0_login"

auth0_blueprint = OAuth2ConsumerBlueprint(
    "auth0", __name__,
    client_id = os.getenv('auth0_client_id'),
    client_secret = os.getenv('auth0_client_secret'),
    base_url = os.getenv('auth0_base_url'),
    token_url = os.getenv('auth0_token_url'),
    authorization_url = os.getenv('auth0_authorization_url')
)

app.register_blueprint(auth0_blueprint, url_prefix="/auth0_login")
