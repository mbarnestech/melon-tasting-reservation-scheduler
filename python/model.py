#import Python modules
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

#---------------------------------------------------------------------#
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///tasting_schedule"
    db.init_app(app)
    return app

app = create_app()
app.app_context().push()

#---------------------------------------------------------------------#

class User(db.Model):
    """A User"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable = False)
    password = db.Column(db.String)

    reservations = db.relationship('Reservation', back_populates='user')
    

    def __repr__(self):
        return f'<User id={self.user_id} name={self.user_name}>'


class Reservation(db.Model):
    """A Reservation for a User"""

    __tablename__ = 'reservations'

    reservation_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable = False)
    appointment = db.Column(db.DateTime, nullable = False)
    status = db.Column(db.String, nullable = False)

    user = db.relationship('User', back_populates='reservations')
    
    def __repr__(self):
        return f'<User id={self.user_id} name={self.user_name}>'
