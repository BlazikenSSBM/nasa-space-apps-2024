from flask import Flask,request,redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy


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
