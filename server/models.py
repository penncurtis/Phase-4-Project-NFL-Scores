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


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    off_rank_2022 = db.Column(db.Integer)
    def_rank_2022 = db.Column(db.Integer)
    points_per_game_2022 = db.Column(db.Float)
    points_allowed_2022 = db.Column(db.Float)
    points_SIV = db.Column(db.Float)
    point_AIV = db.Column(db.Float)

    away_games = db.relationship('Game', backref='away_team', foreign_keys="Game.away_team_id")
    home_games = db.relationship('Game', backref='home_team', foreign_keys="Game.home_team_id")

    win_prediction = db.relationship('Prediction', backref='win_prediction', foreign_keys="Prediction.winning_team_id")
    lose_prediction = db.relationship('Prediction', backref='lose_prediction', foreign_keys="Prediction.winning_team_id")

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

    predictions = db.relationship('Prediction', backref='game')



class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    machine_predicted_score = db.Column(db.Float)
    user_predicted_score = db.Column(db.Float)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

    losing_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    winning_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)




# class Team(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)

#     away_games = db.relationship('Game', backref='away_team', foreign_keys="Game.away_team_id")
#     home_games = db.relationship('Game', backref='home_team', foreign_keys="Game.home_team_id")

#     win_prediction = db.relationship('Prediction', backref='win_prediction', foreign_keys="Prediction.winning_team_id")
#     lose_prediction = db.relationship('Prediction', backref='lose_prediction', foreign_keys="Prediction.winning_team_id")

# class Game(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     away_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
#     home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)

#     predictions = db.relationship('Prediction', backref='game')

# class Prediction(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

#     losing_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
#     winning_team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)