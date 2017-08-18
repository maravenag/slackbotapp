from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/actions", methods=['POST'])
def handleButtons():
    print request.get_data()
    return "Recibi eso!!"