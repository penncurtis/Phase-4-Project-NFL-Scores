#!/usr/bin/env python3

from app import app
from models import db, Team, Game, Prediction


with app.app_context():
    
    Team.query.delete()
    Game.query.delete()
    Prediction.query.delete()

    # Create teams
#     teams_data = [
#     {
#         'team_name': 'Arizona Cardinals',
#         'off_rank_2022': 10,
#         'def_rank_2022': 15,
#         'points_per_game_2022': 26.7,
#         'points_allowed_2022': 21.4,
#         'points_SIV': 28.035,
#         'point_AIV': 22.47
#     },
#     {
#         'team_name': 'Atlanta Falcons',
#         'off_rank_2022': 25,
#         'def_rank_2022': 29,
#         'points_per_game_2022': 19.7,
#         'points_allowed_2022': 25.9,
#         'points_SIV': 16.745,
#         'point_AIV': 22.115
#     },
#     {
#         'team_name': 'Baltimore Ravens',
#         'off_rank_2022': 9,
#         'def_rank_2022': 2,
#         'points_per_game_2022': 28.1,
#         'points_allowed_2022': 19.2,
#         'points_SIV': 32.315,
#         'point_AIV': 13.44
#     },
#     {
#         'team_name': 'Buffalo Bills',
#         'off_rank_2022': 1,
#         'def_rank_2022': 1,
#         'points_per_game_2022': 30.7,
#         'points_allowed_2022': 16.8,
#         'points_SIV': 38.375,
#         'point_AIV': 11.76
#     },
#     {
#         'team_name': 'Carolina Panthers',
#         'off_rank_2022': 30,
#         'def_rank_2022': 6,
#         'points_per_game_2022': 16.8,
#         'points_allowed_2022': 20.2,
#         'points_SIV': 14.875,
#         'point_AIV': 20.17
#     },
#     {
#         'team_name': 'Chicago Bears',
#         'off_rank_2022': 27,
#         'def_rank_2022': 22,
#         'points_per_game_2022': 18.9,
#         'points_allowed_2022': 22.4,
#         'points_SIV': 15.765,
#         'point_AIV': 23.66
#     },
#     {
#         'team_name': 'Cincinnati Bengals',
#         'off_rank_2022': 13,
#         'def_rank_2022': 26,
#         'points_per_game_2022': 24.6,
#         'points_allowed_2022': 25.4,
#         'points_SIV': 25.41,
#         'point_AIV': 30.16
#     },
#     {
#         'team_name': 'Cleveland Browns',
#         'off_rank_2022': 5,
#         'def_rank_2022': 9,
#         'points_per_game_2022': 27.2,
#         'points_allowed_2022': 21.4,
#         'points_SIV': 33.8,
#         'point_AIV': 19.29
#     },
#     {
#         'team_name': 'Dallas Cowboys',
#         'off_rank_2022': 2,
#         'def_rank_2022': 31,
#         'points_per_game_2022': 30.8,
#         'points_allowed_2022': 26.5,
#         'points_SIV': 33.11,
#         'point_AIV': 21.02
#     },
#     {
#         'team_name': 'Denver Broncos',
#         'off_rank_2022': 21,
#         'def_rank_2022': 10,
#         'points_per_game_2022': 21.6,
#         'points_allowed_2022': 20.6,
#         'points_SIV': 19.35,
#         'point_AIV': 17.68
#     },
#     {
#         'team_name': 'Detroit Lions',
#         'off_rank_2022': 32,
#         'def_rank_2022': 27,
#         'points_per_game_2022': 15.8,
#         'points_allowed_2022': 29.8,
#         'points_SIV': 12.72,
#         'point_AIV': 28.96
#     },
#     {
#         'team_name': 'Green Bay Packers',
#         'off_rank_2022': 4,
#         'def_rank_2022': 20,
#         'points_per_game_2022': 27.3,
#         'points_allowed_2022': 23.4,
#         'points_SIV': 28.47,
#         'point_AIV': 21.96
#     },
#     {
#         'team_name': 'Houston Texans',
#         'off_rank_2022': 31,
#         'def_rank_2022': 21,
#         'points_per_game_2022': 15.7,
#         'points_allowed_2022': 26.8,
#         'points_SIV': 14.41,
#         'point_AIV': 20.88
#     },
#     {
#         'team_name': 'Indianapolis Colts',
#         'off_rank_2022': 11,
#         'def_rank_2022': 12,
#         'points_per_game_2022': 25.6,
#         'points_allowed_2022': 20.8,
#         'points_SIV': 26.64,
#         'point_AIV': 17.6
#     },
#     {
#         'team_name': 'Jacksonville Jaguars',
#         'off_rank_2022': 26,
#         'def_rank_2022': 28,
#         'points_per_game_2022': 18.6,
#         'points_allowed_2022': 24.4,
#         'points_SIV': 15.09,
#         'point_AIV': 22.02
#     },
#     {
#         'team_name': 'Kansas City Chiefs',
#         'off_rank_2022': 3,
#         'def_rank_2022': 25,
#         'points_per_game_2022': 29.9,
#         'points_allowed_2022': 26.6,
#         'points_SIV': 32.12,
#         'point_AIV': 20.62
#     },
#     {
#         'team_name': 'Las Vegas Raiders',
#         'off_rank_2022': 14,
#         'def_rank_2022': 32,
#         'points_per_game_2022': 24.9,
#         'points_allowed_2022': 27.2,
#         'points_SIV': 30.66,
#         'point_AIV': 22.94
#     },
#     {
#         'team_name': 'Los Angeles Chargers',
#         'off_rank_2022': 6,
#         'def_rank_2022': 13,
#         'points_per_game_2022': 26.4,
#         'points_allowed_2022': 20.8,
#         'points_SIV': 32.2,
#         'point_AIV': 16.6
#     },
#     {
#         'team_name': 'Los Angeles Rams',
#         'off_rank_2022': 7,
#         'def_rank_2022': 8,
#         'points_per_game_2022': 25.9,
#         'points_allowed_2022': 20.3,
#         'points_SIV': 27.82,
#         'point_AIV': 15.88
#     },
#     {
#         'team_name': 'Miami Dolphins',
#         'off_rank_2022': 23,
#         'def_rank_2022': 11,
#         'points_per_game_2022': 20.3,
#         'points_allowed_2022': 19.4,
#         'points_SIV': 18.05,
#         'point_AIV': 15.4
#     },
#     {
#         'team_name': 'Minnesota Vikings',
#         'off_rank_2022': 16,
#         'def_rank_2022': 16,
#         'points_per_game_2022': 24.3,
#         'points_allowed_2022': 24.4,
#         'points_SIV': 24.72,
#         'point_AIV': 23.84
#     },
#     {
#         'team_name': 'New England Patriots',
#         'off_rank_2022': 15,
#         'def_rank_2022': 7,
#         'points_per_game_2022': 25.4,
#         'points_allowed_2022': 16.7,
#         'points_SIV': 26.76,
#         'point_AIV': 13.52
#     },
#     {
#         'team_name': 'New Orleans Saints',
#         'off_rank_2022': 22,
#         'def_rank_2022': 4,
#         'points_per_game_2022': 21.7,
#         'points_allowed_2022': 21.3,
#         'points_SIV': 24.1,
#         'point_AIV': 11.12
#     },
#     {
#         'team_name': 'New York Giants',
#         'off_rank_2022': 28,
#         'def_rank_2022': 19,
#         'points_per_game_2022': 17.8,
#         'points_allowed_2022': 23.5,
#         'points_SIV': 15.64,
#         'point_AIV': 19.76
#     },
#     {
#         'team_name': 'New York Jets',
#         'off_rank_2022': 29,
#         'def_rank_2022': 30,
#         'points_per_game_2022': 17.1,
#         'points_allowed_2022': 31.3,
#         'points_SIV': 15.39,
#         'point_AIV': 26.14
#     },
#     {
#         'team_name': 'Philadelphia Eagles',
#         'off_rank_2022': 24,
#         'def_rank_2022': 18,
#         'points_per_game_2022': 20.3,
#         'points_allowed_2022': 23.6,
#         'points_SIV': 19.84,
#         'point_AIV': 20.62
#     },
#     {
#         'team_name': 'Pittsburgh Steelers',
#         'off_rank_2022': 17,
#         'def_rank_2022': 14,
#         'points_per_game_2022': 24.4,
#         'points_allowed_2022': 21.8,
#         'points_SIV': 24.68,
#         'point_AIV': 18.16
#     },
#     {
#         'team_name': 'San Francisco 49ers',
#         'off_rank_2022': 18,
#         'def_rank_2022': 5,
#         'points_per_game_2022': 24.8,
#         'points_allowed_2022': 20.7,
#         'points_SIV': 25.74,
#         'point_AIV': 13.76
#     },
#     {
#         'team_name': 'Seattle Seahawks',
#         'off_rank_2022': 8,
#         'def_rank_2022': 23,
#         'points_per_game_2022': 27.5,
#         'points_allowed_2022': 26.3,
#         'points_SIV': 31.75,
#         'point_AIV': 21.84
#     },
#     {
#         'team_name': 'Tampa Bay Buccaneers',
#         'off_rank_2022': 12,
#         'def_rank_2022': 17,
#         'points_per_game_2022': 26.9,
#         'points_allowed_2022': 24.3,
#         'points_SIV': 28.78,
#         'point_AIV': 20.61
#     },
#     {
#         'team_name': 'Tennessee Titans',
#         'off_rank_2022': 19,
#         'def_rank_2022': 24,
#         'points_per_game_2022': 24.6,
#         'points_allowed_2022': 26.6,
#         'points_SIV': 24.92,
#         'point_AIV': 25.54
#     },
#     {
#         'team_name': 'Washington Football Team',
#         'off_rank_2022': 20,
#         'def_rank_2022': 3,
#         'points_per_game_2022': 22.2,
#         'points_allowed_2022': 20.5,
#         'points_SIV': 24.7,
#         'point_AIV': 12.94
#     }
# ]


#     for team_data in teams_data:
#         team = Team(**team_data)
#         db.session.add(team)

    # Create games
#     games_data = [
#         {
#             'date_time': '2023-09-10 20:20',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-09-10 20:20',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'Bank of America Stadium, Charlotte, NC',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'New York Jets'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Giants',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'FedExField, Landover, MD',
#             'home_team': 'Washington Football Team',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Indianapolis Colts',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Pittsburgh Steelers'
#         },
#         {
#             'date_time': '2023-09-11 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Tampa Bay Buccaneers'
#         },
#         {
#             'date_time': '2023-09-11 16:25',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-09-11 16:25',
#             'location': 'State Farm Stadium, Glendale, AZ',
#             'home_team': 'Arizona Cardinals',
#             'away_team': 'San Francisco 49ers'
#         }, 
#         {
#             'date_time': '2023-09-11 16:25',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-09-11 20:20',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-09-11 20:20',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': '2023-09-11 20:20',
#             'location': 'State Farm Stadium, Glendale, AZ',
#             'home_team': 'Arizona Cardinals',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-09-12 20:15',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-09-12 20:15',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-09-15 20:20',
#             'location': 'Paul Brown Stadium, Cincinnati, OH',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'Bank of America Stadium, Charlotte, NC',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Indianapolis Colts',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Washington Football Team'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Kansas City Chiefs'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-09-17 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-09-17 16:05',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Tampa Bay Buccaneers'
#         },
#         {
#             'date_time': '2023-09-17 16:25',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-09-17 20:20',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-09-18 20:15',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-09-22 20:20',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'Bank of America Stadium, Charlotte, NC',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'Washington Football Team'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Indianapolis Colts',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-09-24 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-09-24 16:05',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-09-24 16:25',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-09-24 20:20',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'New York Jets'
#         },
#         {
#             'date_time': '2023-09-25 20:15',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Atlanta Falcons'
#         },
#         {
#             'date_time': '2023-09-28 20:15',
#             'location': 'Lambeau Field, Green Bay, WI',
#             'home_team': 'Green Bay Packers',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': '2023-10-01 09:30',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'Miami Dolphins',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'Bank of America Stadium, Charlotte, NC',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'FedExField, Landover, MD',
#             'home_team': 'Washington Commanders',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-10-01 13:00',
#             'location': 'Paul Brown Stadium, Cincinnati, OH',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-10-01 16:05',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-10-01 16:25',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-10-01 16:25',
#             'location': 'State Farm Stadium, Glendale, AZ',
#             'home_team': 'Arizona Cardinals',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-10-01 20:20',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'New York Jets'
#         },
#         {
#             'date_time': '2023-10-02 20:15',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-10-05 20:15',
#             'location': 'FedExField, Landover, MD',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-10-08 09:30',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-10-08 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Houston Texans',
#             'away_team': 'Atlanta Falcons'
#         },
#         {
#             'date_time': '2023-10-08 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': '2023-10-08 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Tennessee Titans',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-10-08 13:00',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'New York Giants',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-10-08 13:00',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'New England Patriots'
#         },
#         {
#             'date_time': '2023-10-08 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Pittsburgh Steelers'
#         },
#         {
#             'date_time': '2023-10-08 16:05',
#             'location': 'State Farm Stadium, Glendale, AZ',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-10-08 16:05',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-10-08 16:25',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Denver Broncos',
#             'away_team': 'New York Jets'
#         },
#         {
#             'date_time': '2023-10-08 16:25',
#             'location': 'U.S. Bank Stadium, Minneapolis, MN',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Kansas City Chiefs'
#         },
#         {
#             'date_time': '2023-10-08 20:20',
#             'location': "Levi'\s Stadium, Santa Clara, CA",
#             'home_team': 'San Francisco 49ers',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-10-09 20:15',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-10-12 20:15',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-10-15 09:30',
#             'location': 'Nissan Stadium, Nashville, TN',
#             'home_team': 'Tennessee Titans',
#             'away_team': 'Baltimore Ravens'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'Paul Brown Stadium, Cincinnati, OH',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'FirstEnergy Stadium, Cleveland, OH',
#             'home_team': 'Cleveland Browns',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'NRG Stadium, Houston, TX',
#             'home_team': 'Houston Texans',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Miami Dolphins',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': '2023-10-15 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': '2023-10-15 16:05',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'New England Patriots'
#         },
#         {
#             'date_time': '2023-10-15 16:25',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-10-15 16:25',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Jets',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-10-15 20:20',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'Buffalo Bills',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-10-16 20:15',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Chargers',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-10-19 20:15',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-10-22 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Baltimore Ravens'
#         },
#         {
#             'date_time': '2023-10-22 13:00',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-10-22 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Indianapolis Colts',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-10-22 13:00',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-10-22 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Giants',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-10-22 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Atlanta Falcons'
#         },
#         {
#             'date_time': '2023-10-22 16:05',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Pittsburgh Steelers'
#         },
#         {
#             'date_time': '2023-10-22 16:05',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-10-22 16:25',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-10-22 16:25',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-10-22 20:20',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Miami Dolphins',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-10-23 20:15',
#             'location': 'U.S. Bank Stadium, Minneapolis, MN',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-10-26 20:15',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'NRG Stadium, Houston, TX',
#             'home_team': 'Houston Texans',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'U.S. Bank Stadium, Minneapolis, MN',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Jets',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-10-29 13:00',
#             'location': 'Lincoln Financial Field, Philadelphia, PA',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-10-29 16:05',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-10-29 16:25',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-10-29 16:25',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-10-29 16:25',
#             'location': 'Paul Brown Stadium, Cincinnati, OH',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-10-29 20:20',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-10-30 20:15',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': '2023-11-02 20:15',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-11-05 09:30',
#             'location': 'Tottenham Hotspur Stadium, London, England',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'FirstEnergy Stadium, Cleveland, OH',
#             'home_team': 'Cleveland Browns',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'Lambeau Field, Green Bay, WI',
#             'home_team': 'Green Bay Packers',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-11-05 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-11-05 16:05',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Indianapolis Colts',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': '2023-11-05 16:25',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-11-05 16:25',
#             'location': 'AT&T Stadium, Arlington, TX',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-11-05 20:20',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'Buffalo Bills',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': '2023-11-06 20:15',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Jets',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-11-09 20:15',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': '2023-11-12 09:30',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-11-12 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-11-12 13:00',
#             'location': 'Paul Brown Stadium, Cincinnati, OH',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-11-12 13:00',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-11-12 13:00',
#             'location': 'U.S. Bank Stadium, Minneapolis, MN',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-11-12 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-11-12 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-11-12 16:05',
#             'location': 'State Farm Stadium, Glendale, AZ',
#             'home_team': 'Arizona Cardinals',
#             'away_team': 'Atlanta Falcons'
#         },
#         {
#             'date_time': '2023-11-12 16:05',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-11-12 16:25',
#             'location': 'AT&T Stadium, Arlington, TX',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-11-12 16:25',
#             'location': 'FedExField, Landover, MD',
#             'home_team': 'Washington Commanders',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-11-12 20:20',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Jets',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-11-13 20:15',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-11-16 20:15',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'Bank of America Stadium, Charlotte, NC',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'FirstEnergy Stadium, Cleveland, OH',
#             'home_team': 'Cleveland Browns',
#             'away_team': 'Pittsburgh Steelers'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Chargers',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'NRG Stadium, Houston, TX',
#             'home_team': 'Houston Texans',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'Allegiant Stadium, Paradise, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-11-19 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Giants',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-11-19 16:05',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-11-19 16:25',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'New York Jets',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-11-19 16:25',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-11-19 20:20',
#             'location': 'U.S. Bank Stadium, Minneapolis, MN',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-11-20 20:15',
#             'location': 'Lincoln Financial Field, Philadelphia, PA',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'Kansas City Chiefs'
#         },
#         {
#             'date_time': '2023-11-23 12:30',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-11-23 16:30',
#             'location': 'AT&T Stadium, Arlington, TX',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-11-23 20:20',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-11-24 15:00',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Miami Dolphins',
#             'away_team': 'New York Jets'
#         },
#         {
#             'date_time': '2023-11-26 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Atlanta Falcons'
#         },
#         {
#             'date_time': '2023-11-26 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': '2023-11-26 13:00',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-11-26 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-11-26 13:00',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'New England Patriots',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-11-26 13:00',
#             'location': 'Bank of America Stadium, Charlotte, NC',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-11-26 16:05',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-11-26 16:05',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Cleveland Browns',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-11-26 16:25',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-11-26 16:25',
#             'location': 'Bills Stadium, Orchard Park, NY',
#             'home_team': 'Buffalo Bills',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-11-26 20:20',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-11-27 20:15',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': '2023-11-30 20:15',
#             'location': 'AT&T Stadium, Arlington, TX',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'Detroit Lions',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'New York Jets'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Tennessee Titans',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-12-03 13:00',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Washington Commanders',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-12-03 16:05',
#             'location': 'NRG Stadium, Houston, TX',
#             'home_team': 'Houston Texans',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-12-03 16:25',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-12-03 16:25',
#             'location': 'Lincoln Financial Field, Philadelphia, PA',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-12-03 20:20',
#             'location': 'Lambeau Field, Green Bay, WI',
#             'home_team': 'Green Bay Packers',
#             'away_team': 'Kansas City Chiefs'
#         },
#         {
#             'date_time': '2023-12-04 20:15',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': '2023-12-07 20:15',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'New England Patriots',
#             'away_team': 'Pittsburgh Steelers'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'Mercedes-Benz Stadium, Atlanta, GA',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Atlanta Falcons'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'M&T Bank Stadium, Baltimore, MD',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'Baltimore Ravens'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'Paul Brown Stadium, Cincinnati, OH',
#             'home_team': 'Indianapolis Colts',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'FirstEnergy Stadium, Cleveland, OH',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-12-10 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'New York Jets',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-12-10 16:05',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': '2023-12-10 16:05',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'San Francisco 49ers',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-12-10 16:25',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-12-10 16:25',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Los Angeles Chargers',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-12-10 20:20',
#             'location': 'Lincoln Financial Field, Philadelphia, PA',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-12-11 20:15',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Miami Dolphins',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-12-11 20:15',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'Green Bay Packers',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-12-14 20:15',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Los Angeles Chargers',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-12-17 13:00',
#             'location': 'Lambeau Field, Green Bay, WI',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-12-17 13:00',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'New York Jets',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-12-17 13:00',
#             'location': 'Mercedes-Benz Superdome, New Orleans, LA',
#             'home_team': 'New York Giants',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': '2023-12-17 13:00',
#             'location': 'Nissan Stadium, Nashville, TN',
#             'home_team': 'Houston Texans',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': '2023-12-17 16:05',
#             'location': 'State Farm Stadium, Glendale, AZ',
#             'home_team': 'San Francisco 49ers',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': '2023-12-17 16:05',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'Washington Commanders',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-12-17 16:25',
#             'location': 'Highmark Stadium, Orchard Park, NY',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-12-17 16:25',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-12-17 20:20',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-12-18 20:15',
#             'location': 'Gillette Stadium, Foxborough, MA',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'New England Patriots'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-12-21 20:15',
#             'location': 'SoFi Stadium, Inglewood, CA',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Los Angeles Rams'
#         },
#         {
#             'date_time': '2023-12-23 16:30',
#             'location': 'Heinz Field, Pittsburgh, PA',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Pittsburgh Steelers'
#         },
#         {
#             'date_time': '2023-12-23 20:00',
#             'location': 'Bills Stadium, Orchard Park, NY',
#             'home_team': 'Buffalo Bills',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': '2023-12-24 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-12-24 13:00',
#             'location': 'Lambeau Field, Green Bay, WI',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': '2023-12-24 13:00',
#             'location': 'NRG Stadium, Houston, TX',
#             'home_team': 'Cleveland Browns',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-12-24 13:00',
#             'location': 'Ford Field, Detroit, MI',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': '2023-12-24 13:00',
#             'location': 'FedExField, Landover, MD',
#             'home_team': 'New York Jets',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-12-24 13:00',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Tennessee Titans',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-12-24 16:05',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-12-24 16:25',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Arizona Cardinals',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-12-24 16:25',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': '2023-12-25 20:15',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'New England Patriots',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-12-25 13:00',
#             'location': 'Allegiant Stadium, Las Vegas, NV',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': '2023-12-25 16:30',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-12-25 20:15',
#             'location': "Levi's Stadium, Santa Clara, CA",
#             'home_team': 'Baltimore Ravens',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': '2023-12-28 20:15',
#             'location': 'FirstEnergy Stadium, Cleveland, OH',
#             'home_team': 'New York Jets',
#             'away_team': 'Cleveland Browns'
#         },
#         {
#             'date_time': '2023-12-30 20:15',
#             'location': 'AT&T Stadium, Arlington, TX',
#             'home_team': 'Detroit Lions',
#             'away_team': 'Dallas Cowboys'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'Hard Rock Stadium, Miami Gardens, FL',
#             'home_team': 'Miami Dolphins',
#             'away_team': 'Baltimore Ravens'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'Bills Stadium, Orchard Park, NY',
#             'home_team': 'New England Patriots',
#             'away_team': 'Buffalo Bills'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'Soldier Field, Chicago, IL',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'Chicago Bears'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'NRG Stadium, Houston, TX',
#             'home_team': 'Tennessee Titans',
#             'away_team': 'Houston Texans'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'Lucas Oil Stadium, Indianapolis, IN',
#             'home_team': 'Las Vegas Raiders',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'TIAA Bank Field, Jacksonville, FL',
#             'home_team': 'Carolina Panthers',
#             'away_team': 'Jacksonville Jaguars'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'MetLife Stadium, East Rutherford, NJ',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'Lincoln Financial Field, Philadelphia, PA',
#             'home_team': 'Arizona Cardinals',
#             'away_team': 'Philadelphia Eagles'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': 'Raymond James Stadium, Tampa, FL',
#             'home_team': 'New Orleans Saints',
#             'away_team': 'Tampa Bay Buccaneers'
#         },
#         {
#             'date_time': '2023-12-31 13:00',
#             'location': "Levi's Stadium, Santa Clara, CA",
#             'home_team': 'San Francisco 49ers',
#             'away_team': 'Washington Commanders'
#         },
#         {
#             'date_time': '2023-12-31 16:05',
#             'location': 'Lumen Field, Seattle, WA',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Seattle Seahawks'
#         },
#         {
#             'date_time': '2023-12-31 16:25',
#             'location': 'Empower Field at Mile High, Denver, CO',
#             'home_team': 'Los Angeles Chargers',
#             'away_team': 'Denver Broncos'
#         },
#         {
#             'date_time': '2023-12-31 16:25',
#             'location': 'Arrowhead Stadium, Kansas City, MO',
#             'home_team': 'Cincinnati Bengals',
#             'away_team': 'Kansas City Chiefs'
#         },
#         {
#             'date_time': '2023-12-31 20:20',
#             'location': 'U.S. Bank Stadium, Minneapolis, MN',
#             'home_team': 'Green Bay Packers',
#             'away_team': 'Minnesota Vikings'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Seattle Seahawks',
#             'away_team': 'Arizona Cardinals'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Pittsburgh Steelers',
#             'away_team': 'Baltimore Ravens'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Tampa Bay Buccaneers',
#             'away_team': 'Carolina Panthers'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Cleveland Browns',
#             'away_team': 'Cincinnati Bengals'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Minnesota Vikings',
#             'away_team': 'Detroit Lions'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Chicago Bears',
#             'away_team': 'Green Bay Packers'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Houston Texans',
#             'away_team': 'Indianapolis Colts'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Kansas City Chiefs',
#             'away_team': 'Los Angeles Chargers'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Denver Broncos',
#             'away_team': 'Las Vegas Raiders'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Buffalo Bills',
#             'away_team': 'Miami Dolphins'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'New York Jets',
#             'away_team': 'New England Patriots'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Atlanta Falcons',
#             'away_team': 'New Orleans Saints'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Philadelphia Eagles',
#             'away_team': 'New York Giants'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Los Angeles Rams',
#             'away_team': 'San Francisco 49ers'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Jacksonville Jaguars',
#             'away_team': 'Tennessee Titans'
#         },
#         {
#             'date_time': 'TBD',
#             'location': 'TBD',
#             'home_team': 'Dallas Cowboys',
#             'away_team': 'Washington Commanders'
#         }
# ]

#     for game_data in games_data:
#         game = Game(**game_data)
#         db.session.add(game)
    
#         team1 = Team.query.filter_by(team_name=game_data['home_team']).first()
#         team2 = Team.query.filter_by(team_name=game_data['away_team']).first()

#         predicted_score_team1 = (team1.points_SIV + team2.point_AIV) / 2
#         predicted_score_team2 = (team2.points_SIV + team1.point_AIV) / 2

#         single_score = f"{((team1.points_SIV + team2.point_AIV) / 2)) - ((team2.points_SIV + team1.point_AIV) / 2)}

#         prediction_data = {
#             'machine_predicted_score': f"{predicted_score_team1:.2f}-{predicted_score_team2:.2f}",
#             'game': game,
#             'home_team': team1,
#             'away_team': team2
#         }

#         prediction = Prediction(**prediction_data)
#         db.session.add(prediction)

    db.session.commit()
    print("🌱 Teams, Games, and Predictions successfully seeded! 🌱")
