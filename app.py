from flask import Flask
from configuration import Configuration
"""app - объект фласка, который запускает web сервер"""
app = Flask(__name__)

app.config.from_object(Configuration)
