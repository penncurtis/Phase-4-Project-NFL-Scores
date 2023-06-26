from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Team, Game, Prediction

api = Api(app)

class Teams(Resource):
    def get(self):
        teams = Team.query.all()
        response_body = [team.to_dict() for team in teams]
        return make_response(jsonify(response_body), 200)
    
api.add_resource(Teams, '/teams')

class TeamById(Resource):
    def get(self, id):
        team = Team.query.get(id)
        if not team:
            response_body = {"error": "Team not found"}
            status = 404
        else:
            response_body = team.to_dict()
            status = 200
        return make_response(jsonify(response_body), status)
    
api.add_resource(TeamById, '/teams/<int:id>')

class Games(Resource):
    def get(self):
        games = Game.query.all()
        response_body = [game.to_dict() for game in games]
        return make_response(jsonify(response_body), 200)
    
api.add_resource(Games, '/games')

class GameById(Resource):
    def get(self, id):
        game = Game.query.get(id)
        if not game:
            response_body = {"error": "Game not found"}
            status = 404
        else:
            response_body = game.to_dict()
            status = 200
        return make_response(jsonify(response_body), status)

api.add_resource(GameById, '/games/<int:id>')

class Predictions(Resource):
    def get(self):
        predictions = Prediction.query.all()
        response_body = [prediction.to_dict() for prediction in predictions]
        return make_response(jsonify(response_body), 200)
    
api.add_resource(Predictions, '/predictions')

class PredictionById(Resource):
    def get(self, id):
        prediction = Prediction.query.get(id)
        if not prediction:
            response_body = {"error": "Prediction not found"}
            status = 404
        else:
            response_body = prediction.to_dict()
            status = 200
        return make_response(jsonify(response_body), status)

    def post(self):
        data = request.get_json()
        game_id = data.get('game_id')
        if not game_id:
            response_body = {"error": "Game ID is required"}
            return make_response(jsonify(response_body), 400)

        game = Game.query.get(game_id)
        if not game:
            response_body = {"error": "Game not found"}
            return make_response(jsonify(response_body), 404)

        new_prediction = Prediction(
            machine_predicted_score=data.get('machine_predicted_score'),
            user_predicted_score=data.get('user_predicted_score'),
            game=game
        )

        db.session.add(new_prediction)
        db.session.commit()

        response_body = new_prediction.to_dict()
        return make_response(jsonify(response_body), 201)

    def patch(self, id):
        prediction = Prediction.query.get(id)
        if not prediction:
            response_body = {"error": "Prediction not found"}
            return make_response(jsonify(response_body), 404)

        data = request.get_json()
        game_id = data.get('game_id')
        if game_id:
            game = Game.query.get(game_id)
            if not game:
                response_body = {"error": "Game not found"}
                return make_response(jsonify(response_body), 404)
            prediction.game = game

        if 'machine_predicted_score' in data:
            prediction.machine_predicted_score = data.get('machine_predicted_score')

        if 'user_predicted_score' in data:
            prediction.user_predicted_score = data.get('user_predicted_score')

        db.session.commit()

        response_body = prediction.to_dict()
        return make_response(jsonify(response_body), 200)

api.add_resource(PredictionById, '/predictions/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)