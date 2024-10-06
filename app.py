from flask import Flask, render_template, request, jsonify, make_response
from flask import Flask,request,redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from EmailLandSat import send_simple_message


app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'

db= SQLAlchemy(app)

#models
class Main(db.Model):
    email = db.Column(db.String(255), primary_key=True)  # Primary key
    latitudeA = db.Column(db.Numeric(9, 6), nullable=True)  # Decimal for latitudeA
    longitudeA = db.Column(db.Numeric(9, 6), nullable=True)  # Decimal for longitudeA
    latitudeB = db.Column(db.Numeric(9, 6), nullable=True)  # Decimal for latitudeB
    longitudeB = db.Column(db.Numeric(9, 6), nullable=True)  # Decimal for longitudeB

    # Constraints are added in a more declarative way using SQLAlchemy
    __table_args__ = (
        db.CheckConstraint('latitudeA BETWEEN -90 AND 90', name='lat_rangeA'),
        db.CheckConstraint('longitudeA BETWEEN -180 AND 180', name='lon_rangeA'),
        db.CheckConstraint('latitudeB BETWEEN -90 AND 90', name='lat_rangeB'),
        db.CheckConstraint('longitudeB BETWEEN -180 AND 180', name='lon_rangeB'),
        db.CheckConstraint("email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'", name='email_regex')
    )
def create_tables():
    db.create_all()

app = Flask(__name__)

@app.route("/")
def index():
#	return render_template("index.html")
    return "Hello, World!"

@app.route('/register')
def register():
    return render_template("register.html", name="")

@app.route('/getEmail',methods=['POST','GET'])
def getEmail():
    if request.method=='POST':
        user=request.form['email']
        latitudeA= request.form['latitudeA']
        longtitudeA=request.form['longtitudeA']
        latitudeB=request.form['latitudeB']
        longtitudeB=request.form['longtitudeB']

        existing_user = Main.query.filter_by(email=user).first()

        if existing_user:
            return render_template("register.html", name='email accepted')
        else:
            new_user = Main(email=user, latitudeA=latitudeA, longitudeA=longtitudeA, latitudeB=latitudeB, longitudeB=longtitudeB)
            db.session.add(new_user)
            db.session.commit()
            return render_template("register.html", name="email accepted")
    
    return render_template("register.html",name= "please enter valid detials")

send_simple_message()

if __name__ == '__main__':
    app.run(debug=True)