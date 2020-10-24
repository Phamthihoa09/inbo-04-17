from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/v2')
def hello_world_v2():
    return 'Another text'

@app.route('/Ml9799')
def Ml9799():
    return 'Ml9799 write in VScode'

@app.route('/edmanuk')
def edmanuk():
    return 'Good day!!!'

@app.route('/capchik')
def capchik():
    return 'CAPCHIK cool task'

@app.route('/shistick98')
def shitick98():
    return 'I am Dmitrii Shesterikov, inbo-04-17'

@app.route('/user937')
def user937():
    return 'user937 task'

@app.route('/Kubirill')
def kubirill():
    return 'He is NintendoBoy'

@app.route('/de4d10ck')
def about():
    return 'Welcome to my page'

@app.route('/megurt')
def megurtfunc():
    return 'test task'
