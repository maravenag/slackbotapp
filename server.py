from flask import Flask
from flask import request
import sys
import simplejson as json

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route("/actions", methods=['POST'])
def handleButtons():
    data = request.form['payload'] #getting payload data
    data = json.loads(data)
    username=data['user']['name']
    userid=data['user']['id']
    return "Muchas gracias <@{0}> por tu respuesta".format(userid)