from flask import Flask , request, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_manager, login_user, logout_user, login_required, UserMixin)


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SECRET_KEY'] = 'mysecretkey'

db = SQLAlchemy(app)
login_manager = LoginManager()

class User(UserMixin,db.Model):
    email  = db.Column(db.String(80), unique=True, nullable = False, primary_key = True)
    name  = db.Column(db.String(80), unique=True, nullable = False)
    password  = db.Column(db.String(80), nullable = False)

class Theatre(db.Model):
    seat_number  = db.Column(db.String(80), unique=True, nullable = False, primary_key = True)
    price  = db.Column(db.String(80), unique=True, nullable = False)
    status  = db.Column(db.Integer, nullable = False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def test_connection():
    with app.app_context():
        db.create_all()
        app.run(debug=True)

##Routes
@app.route
def logout():
    session.clear()
    return

@app.route('/user/signin', methods = ['POST'])
def signin():
    if(request.method == 'POST'):
        req = request.get_json()
        # name = req['name']
        email = req['email']
        password = req['password']
        check_user = User.query.filter_by(email=email).first()
        if(check_user is not None):
            if(check_user.password == password):
                login_user(check_user)
                return "Login Successful"
            else: 
                return "Incorrect Password entered"
        else:
            return "User not found"

@app.route('/user/signup', methods = ['POST'])
def signup():
    if(request.method == 'POST'):
        req = request.get_json()
        name = req['name']
        email = req['email']
        password = req['password']
        # check_user = User.query.filter_by(name=name).first()
        obj = User(email=email,name=name,password=password)
        db.session.add(obj)
        db.session.commit()
        return "Signup Successful"
    else:
        return "Signup Unsuccessful"

@login_required
@app.route('/seats/available')
def allseats():
    count = 0
    seat_list = []
    templist = []
    seats_avail = Theatre.query()
    for item in seats_avail:
        if item.status == 0:
            count = count+1
        templist.append(item.seat_number)
        templist.append(item.price)
        seat_list.append(templist.copy())
        templist.clear()
    return jsonify(**{'seats': seat_list, 'seatsAvailable': count})

@login_required
@app.route('/seats/booked')
def bookedseats():
    count = 0
    seat_list = []
    templist = []
    seats_avail = Theatre.query()
    for item in seats_avail:
        if item.status == 1:
            count = count+1
        templist.append(item.seat_number)
        templist.append(item.price)
        seat_list.append(templist.copy())
        templist.clear()
    return jsonify(**{'seats': seat_list, 'seatsAvailable': count})

test_connection()