from flask import Blueprint
from flask import flash, redirect, render_template, request, session, url_for
from sqlalchemy.orm import sessionmaker
from wtforms import ValidationError

from models import *

auth_app = Blueprint('auth_app',
                     __name__,
                     static_folder='static',
                     template_folder='templates'
                     )
# По хорошему нужно рефакторить, чтобы все ссылки и другие настройки брались из конфигурационного файла или
# переменных среды
engine = create_engine('sqlite:///auth/users.db', echo=True)


@auth_app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html',
                               log_out=False)


@auth_app.route('/registration', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        db_session = sessionmaker(bind=engine)
        s = db_session()
        POST_USERNAME = str(request.form['username'])
        if s.query(User).filter(User.username.in_(POST_USERNAME)).first():
            return ValidationError("Username already exists")
        user = User(POST_USERNAME,
                    password=str(request.form['password']),
                    first_name=str(request.form['first_name']),
                    last_name=str(request.form['last_name']),
                    middle_name=str(request.form['middle_name']),
                    )
        s.add(user)
        s.commit()
        flash("Registration completed successfully")
        return redirect(url_for('home'))
    else:
        return render_template('registration.html')


@auth_app.route('/login', methods=['POST'])
def login():
    POST_USERNAME = str(request.form['username'])
    POST_PASSWORD = calculate_digest(str(request.form['password']))

    db_session = sessionmaker(bind=engine)
    s = db_session()
    query = s.query(User).filter(User.username.in_([POST_USERNAME]),
                                 User.password.in_([POST_PASSWORD]))
    result = query.first()
    if result:
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()


@auth_app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
