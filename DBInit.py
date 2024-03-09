from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from appconfig import config
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['DATASOURCEURL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)