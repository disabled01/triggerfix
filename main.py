import os
import requests
from flask import *
from threading import Thread

def check(file, IPS):
    with open(file, 'r') as filed:
        data = filed.read()
        if IPS in str(data):
            return True
        else:
            return False

def checkid(file, IDKEY):
    with open(file, 'r') as filed:
        data = filed.read()
        if IDKEY in str(data):
            return True
        else:
            return False

os.system('set FLASK_ENV=development')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ipget")
def GETIP():
    data = request.args
    key = data.get("key")
    ip = data.get("ip")
    ID = data.get("ID")
    IPS = f'{{"ID": "{ID}", "IP": "{ip}", "ID": "{ID}"}}'
    file = key +'.txt'

    if os.path.exists(file)==False:
        try:check(file=file, IPS=IPS)
        except:
            with open(file, 'w') as file:
                file.write(IPS)
    else:
        return "connected"

@app.route("/ipcheck")
def CHECKIP():
    data = request.args
    key = data.get("key")
    ip = data.get("ip")
    ID = data.get("ID")
    file = key + '.txt'
    if os.path.exists(file) == True:
        uu = f'{{"ID": "{ID}"}}'
        uut = uu[1:]
        uuv = uut[:-1]
        if checkid(file=file, IDKEY=uuv) == True:
            IPS = f'{{"ID": "{ID}", "IP": "{ip}", "ID": "{ID}"}}'
            with open(file, 'w') as filedt:
                filedt.write(IPS)
            return "notconected"
        else:
            return "conected"
    else:
        IPS = f'{{"ID": "{ID}", "IP": "{ip}", "ID": "{ID}"}}'
        with open(file, 'w') as filedt:
            filedt.write(IPS)
        return "notconected"

@app.route("/deletekey")
def DELETKEY():
    data = request.args
    key = data.get("key")
    file = key + '.txt'

    if os.path.exists(file) == True:
        os.remove(file)
        return "keydeleted"
    else:
        return "nokey"

def run():
    app.run("0.0.0.0", 9091)

t = Thread(target=run)
t.start()
