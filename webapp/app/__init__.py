from flask import Flask

t_app = Flask(__name__)
t_app.config.from_object('config')

from app import views
