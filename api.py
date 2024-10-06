from flask import Flask, render_template, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from skyfield.api import EarthSatellite, load
import numpy as np
from EmailLandSat import send_simple_message
from flask import Flask,request,redirect
from flask.templating import render_template
import schedule
import time


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

        existing_user = Main.query.filter_by(email=user).first()

        if existing_user:
            return render_template("register.html", name='email accepted')
        else:
            new_user = Main(email=user, latitudeA=latitudeA, longitudeA=longtitudeA, )
            db.session.add(new_user)
            db.session.commit()
            return render_template("register.html", name="email accepted")
    
    return render_template("register.html",name= "please enter valid detials")


if __name__ == '__main__':
    app.run(debug=True)

@app.route('/calculate_time/<email>', methods=['GET'])
def calculate_time(email):
    # Fetch coordinates from the database
    entry = Main.query.filter_by(email=email).first()
    if not entry:
        return jsonify({'error': 'Entry not found'}), 404
    
    line1 = "1 39084U 13008A   21264.43259861  .00000150  00000-0  00000-0 0  9997"
    line2 = "2 39084  98.1864 193.5981 0001274  89.4485 270.6777 14.57100866396183"
    satellite = EarthSatellite(line1, line2, 'Landsat 8', load.timescale())

    # Get the current time
    ts = load.timescale()
    current_time = ts.now()

    target_latitude = entry.latitudeA
    target_longitude = entry.longitudeA

    time_difference = None
    for i in range(1440):  # Check every minute for the next 24 hours (1440 minutes)
        future_time = current_time + i * 60  # Increment by 1 minute
        geocentric_future = satellite.at(future_time)

        # Calculate distance to target coordinates
        target_position = geocentric_future.subpoint()
        distance = np.sqrt((target_position.latitude.degrees - target_latitude) ** 2 +
                           (target_position.longitude.degrees - target_longitude) ** 2)

        # Set a threshold distance to consider as "reached"
        if distance < 1:  # 1 degree threshold 
            actual_time_difference = (future_time - current_time).total_seconds() / 3600
            
            if actual_time_difference == 24:  # Check if the time difference is exactly 24 hours
                time_difference = future_time.utc_strftime('%Y-%m-%d %H:%M:%S')
                
                send_simple_message()
                break

    
    if time_difference:
        return jsonify({'reach_time': time_difference}), 200
    else:
        return jsonify({'error': 'The satellite will not reach the target coordinates in the next 24 hours.'}), 200

if __name__ == '__main__':
    create_tables()  # Create tables if they don't exist
    app.run(debug=True)