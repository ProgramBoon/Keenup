import sys
from flask import Flask
import os
sys.path.append(os.getcwd()+'/Keenup.lib')
import sne
import database

app = Flask(__name__)

@app.route("/")
def hello_world():
    p = database.Database()
    x = str(p.alarmlast())
    y = x.replace("), (", "<br>")
    x = y.replace('[(', '')
    y = x.replace(')]', '')
    return y

