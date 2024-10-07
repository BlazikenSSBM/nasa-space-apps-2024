from flask import Flask, render_template, request, jsonify, make_response, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from skyfield.api import EarthSatellite, load
import numpy as np
from EmailLandSat import send_simple_message
from flask import Flask,request,redirect
from flask.templating import render_template
import schedule
from apscheduler.schedulers.background import BackgroundScheduler
import time
import get_landsat_api_data
from get_landsat_api_data import datasetSearch
import datetime


app= Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///app.db'

db= SQLAlchemy(app)

#models
class Main(db.Model):
    email = db.Column(db.String(255), primary_key=True)  # Primary key
    latitude = db.Column(db.Numeric(9, 6), nullable=True)  # Decimal for latitude
    longitude = db.Column(db.Numeric(9, 6), nullable=True)  # Decimal for longitude


    # Constraints are added in a more declarative way using SQLAlchemy
    __table_args__ = (
        db.CheckConstraint('latitude BETWEEN -90 AND 90', name='lat_range'),
        db.CheckConstraint('longitude BETWEEN -180 AND 180', name='lon_range'),
        db.CheckConstraint("email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$'", name='email_regex')
    )
def create_tables():
    db.create_all()

app = Flask(__name__)

@app.route("/")
def index_route():
    return send_from_directory('./svelte/build', 'index.html')

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory('./svelte/build', path)

@app.route('/register')
def register():
    return render_template("register.html", name="")

@app.route('/getEmail',methods=['POST','GET'])
def getEmail():
    if request.method=='POST':
        user=request.form['email']
        latitude= request.form['latitude']
        longtitude=request.form['longtitude']


        existing_user = Main.query.filter_by(email=user).first()

        if existing_user:
            return redirect("http://localhost:5173/notifications", name="email already exists")
        else:
            new_user = Main(email=user, latitude=latitude, longitude=longtitude)
            db.session.add(new_user)
            db.session.commit()
            return redirect("http://localhost:5173/notifications", name="email added to notification list")
    
    return redirect("http://localhost:5173/notifications", name= "please enter valid detials")

@app.route('/getCoordinates', methods=['POST','GET'])
def getCoordinates():
    if request.method == 'POST':
        coordinates = [float(request.form['latitude']), float(request.form['longitude'])]
        x = str(datetime.datetime.now())
        x[:10]
        response = datasetSearch(coordinate=coordinates, startTime="2000-01-01", endTime=x, maxCloudCover=100, minCloudCover=0, maxResults=1000)
    return redirect(response[0])   

@app.route('/getCoordinatesAndDate', methods=['POST','GET'])
def getCoordinatesAndDate():
    if request.method == 'POST':
        coordinates = [float(request.form['latitude']), float(request.form['longitude'])]
        date = request.form['date']
        response = datasetSearch(coordinate=coordinates, startTime="2000-01-01", endTime=date, maxCloudCover=100, minCloudCover=0, maxResults=1000)
        print(response)
    return redirect('http://localhost:5173/detailed')   


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

    target_latitude = entry.latitude
    target_longitude = entry.longitude

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
                
                send_simple_message(email, "Satellite will reach the target coordinates in 24 hours", f"The satellite will reach the target coordinates at {time_difference}")
                break

    
    if time_difference:
        return jsonify({'reach_time': time_difference}), 200
    else:
        return jsonify({'error': 'The satellite will not reach the target coordinates in the next 24 hours.'}), 200

def continuous_check():
    with app.app_context():  # Flask context needed for database operations
        entries = Main.query.all()
        for entry in entries:
            calculate_time(entry.email)  # Call the satellite calculation function for each email

# Set up a background scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=continuous_check, trigger="interval", seconds=3600)  # Check every 10 minutes
scheduler.start()


if __name__ == '__main__':
    app.run(debug=True)