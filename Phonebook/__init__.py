from flask import Flask
from config import Config
from .auth.routes import auth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


app.register_blueprint(auth)

app.config.from_object(Config)