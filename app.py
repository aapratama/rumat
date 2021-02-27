from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return 'rumat is'+' coming...'

@app.route('/test', methods=['POST'])
def testPostRequest():
    return request.form['name']

@app.route('/api')
def api():
    return {
        "message": "im an api"
    }