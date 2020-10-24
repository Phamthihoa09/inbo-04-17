from flask import Flask
from flask import flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from models import *

app = Flask(__name__, static_folder='static')
engine = create_engine('sqlite:///main.db', echo=True)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html',
                               log_out=False)


@app.route('/login', methods=['POST'])
def do_admin_login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = calculate_digest(str(request.form['password']))

    Session = sessionmaker(bind=engine)
    s = Session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]),
                                 User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True, port=4000)
