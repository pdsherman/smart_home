
from flask import Flask
from app.config import Config
from app.fan import setup


app = Flask(__name__)
app.config.from_object(Config)
setup()

from app import routes
