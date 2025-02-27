from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests as r
import json as j

from codinglearning.ryan.ryan import ryan_blueprint
from codinglearning.lola.lola import lola_blueprint
from codinglearning.nick.nick import nick_blueprint
from codinglearning.micheal.micheal import micheal_blueprint
from codinglearning.valerie.valerie import valerie_blueprint


app = Flask(__name__)

app.register_blueprint(ryan_blueprint)
app.register_blueprint(lola_blueprint)
app.register_blueprint(nick_blueprint)
app.register_blueprint(micheal_blueprint)
app.register_blueprint(valerie_blueprint)


app.config['SECRET_KEY'] = 'I<+g/P2N$}0GXO00'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
# IMPORTANT - GENERATES CSRF TOKEN
csrf = CSRFProtect(app)
csrf.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin, db.Model):  # Creates columns inside of the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)  # username column
    email = db.Column(db.String(50), unique=True)  # email column
    password = db.Column(db.String(80))  # password column


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])


@app.route('/')
def index():
    # Gets the api data from web
    x = r.get("https://uselessfacts.jsph.pl/random.json?language=en")
    data = j.loads(x.content)  # Fetch rest api data
    fact = data.get("text")  # Fetch rest api data
    return render_template("index.html", fact=fact)  # Fetch rest api data


@app.route('/leaderboards')
def leaderboards():
    return render_template("leaderboards.html")


@app.route('/easteregg1')
def easteregg():
    return render_template('easteregg.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return render_template('invalid.html', form=form)
    # return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        # redirect to page when user is created
        return render_template('usercreatedredirect.html')
    # return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'
    return render_template('signup.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/future')
def future():
    return render_template('futuregames.html')


if __name__ == "__main__":
    app.run(debug=True)

# yolo
