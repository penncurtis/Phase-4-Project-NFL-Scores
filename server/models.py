from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

from app import db

# Models
class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
    off_rank_2022 = db.Column(db.Integer)
    def_rank_2022 = db.Column(db.Integer)
    points_per_game_2022 = db.Column(db.Float)
    points_allowed_2022 = db.Column(db.Float)

    games = db.relationship('Game', backref='team')
    predictions = db.relationship('Prediction', backref='team')

    def serialize(self):
        return {
            'id': self.id,
            'team_name': self.team_name,
            'off_rank_2022': self.off_rank_2022,
            'def_rank_2022': self.def_rank_2022,
            'points_per_game_2022': self.points_per_game_2022,
            'points_allowed_2022': self.points_allowed_2022
        }
    
    @validates('team_name')
    def validate_name(self, key, value):
        if len(value) < 5:
            raise ValueError(f"{key} must be at least 5 characters long.")
        return value

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    matchup = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    predictions = db.relationship('Prediction', backref='game')

    def serialize(self):
        return {
            'id': self.id,
            'game_date': str(self.game_date),
            'location': self.location,
            'matchup': self.matchup
        }

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_predicted_score = db.Column(db.Float)
    user_predicted_score = db.Column(db.Float)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    game = db.relationship('Game', backref=db.backref('predictions'))
    team = db.relationship('Team', backref=db.backref('predictions'))

    def serialize(self):
        return {
            'id': self.id,
            'machine_predicted_score': self.machine_predicted_score,
            'user_predicted_score': self.user_predicted_score,
            'game_id': self.game_id,
            'team_id': self.team_id
        }
    
    @validates('machine_predicted_score')
    def validate_name(self, key, value):
        if not isinstance(value, int):
            raise ValueError(f"{key} must be integer")
        return value
