from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v2')
def hello_world_v2():
    return 'Another text'

@app.route('/capchik')
def capchik():
    return 'CAPCHIK task'

@app.route('/user937')
def user937():
    return 'user937 task'
