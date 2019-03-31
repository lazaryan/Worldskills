from flask import Flask
from conf import Conf


app = Flask(__name__)
app.config.from_object(Conf)
