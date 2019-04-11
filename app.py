from flask import Flask
from configuration import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
