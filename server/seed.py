#!/usr/bin/env python3

from app import app
from models import db, Team, Game

with app.app_context():
    
    Team.query.delete()
    Game.query.delete()

    # Create teams
    teams_data = [
        {
            'team_name': 'Arizona Cardinals',
            'off_rank_2022': 10,
            'def_rank_2022': 15,
            'points_per_game_2022': 26.7,
            'points_allowed_2022': 21.4
        },
        {
            'team_name': 'Atlanta Falcons',
            'off_rank_2022': 25,
            'def_rank_2022': 29,
            'points_per_game_2022': 19.7,
            'points_allowed_2022': 25.9
        },
        {
            'team_name': 'Baltimore Ravens',
            'off_rank_2022': 9,
            'def_rank_2022': 2,
            'points_per_game_2022': 28.1,
            'points_allowed_2022': 19.2
        },
        {
            'team_name': 'Buffalo Bills',
            'off_rank_2022': 1,
            'def_rank_2022': 1,
            'points_per_game_2022': 30.7,
            'points_allowed_2022': 16.8
        },
        {
            'team_name': 'Carolina Panthers',
            'off_rank_2022': 30,
            'def_rank_2022': 6,
            'points_per_game_2022': 16.8,
            'points_allowed_2022': 20.2
        },
        {
            'team_name': 'Chicago Bears',
            'off_rank_2022': 27,
            'def_rank_2022': 22,
            'points_per_game_2022': 18.9,
            'points_allowed_2022': 22.4
        },
        {
            'team_name': 'Cincinnati Bengals',
            'off_rank_2022': 13,
            'def_rank_2022': 26,
            'points_per_game_2022': 24.6,
            'points_allowed_2022': 25.4
        },
        {
            'team_name': 'Cleveland Browns',
            'off_rank_2022': 5,
            'def_rank_2022': 9,
            'points_per_game_2022': 27.2,
            'points_allowed_2022': 21.4
        },
        {
            'team_name': 'Dallas Cowboys',
            'off_rank_2022': 2,
            'def_rank_2022': 31,
            'points_per_game_2022': 30.8,
            'points_allowed_2022': 26.5
        },
        {
            'team_name': 'Denver Broncos',
            'off_rank_2022': 21,
            'def_rank_2022': 17,
            'points_per_game_2022': 20.9,
            'points_allowed_2022': 21.8
        },
        {
            'team_name': 'Detroit Lions',
            'off_rank_2022': 32,
            'def_rank_2022': 30,
            'points_per_game_2022': 16.9,
            'points_allowed_2022': 29.8
        },
        {
            'team_name': 'Green Bay Packers',
            'off_rank_2022': 6,
            'def_rank_2022': 3,
            'points_per_game_2022': 27.5,
            'points_allowed_2022': 21.8
        },
        {
            'team_name': 'Houston Texans',
            'off_rank_2022': 29,
            'def_rank_2022': 32,
            'points_per_game_2022': 19.8,
            'points_allowed_2022': 30.2
        },
        {
            'team_name': 'Indianapolis Colts',
            'off_rank_2022': 23,
            'def_rank_2022': 5,
            'points_per_game_2022': 22.8,
            'points_allowed_2022': 20.4
        },
        {
            'team_name': 'Jacksonville Jaguars',
            'off_rank_2022': 31,
            'def_rank_2022': 24,
            'points_per_game_2022': 15.7,
            'points_allowed_2022': 28.6
        },
        {
            'team_name': 'Kansas City Chiefs',
            'off_rank_2022': 1,
            'def_rank_2022': 16,
            'points_per_game_2022': 30.2,
            'points_allowed_2022': 21.8
        },
        {
            'team_name': 'Las Vegas Raiders',
            'off_rank_2022': 11,
            'def_rank_2022': 28,
            'points_per_game_2022': 25.2,
            'points_allowed_2022': 25.3
        },
        {
            'team_name': 'Los Angeles Chargers',
            'off_rank_2022': 8,
            'def_rank_2022': 12,
            'points_per_game_2022': 28.3,
            'points_allowed_2022': 23.7
        },
        {
            'team_name': 'Los Angeles Rams',
            'off_rank_2022': 3,
            'def_rank_2022': 8,
            'points_per_game_2022': 29.6,
            'points_allowed_2022': 22.7
        },
        {
            'team_name': 'Miami Dolphins',
            'off_rank_2022': 19,
            'def_rank_2022': 14,
            'points_per_game_2022': 23.6,
            'points_allowed_2022': 23.4
        },
        {
            'team_name': 'Minnesota Vikings',
            'off_rank_2022': 14,
            'def_rank_2022': 19,
            'points_per_game_2022': 24.4,
            'points_allowed_2022': 25.2
        },
        {
            'team_name': 'New England Patriots',
            'off_rank_2022': 8,
            'def_rank_2022': 4,
            'points_per_game_2022': 28.5,
            'points_allowed_2022': 19.3
        },
        {
            'team_name': 'New Orleans Saints',
            'off_rank_2022': 17,
            'def_rank_2022': 7,
            'points_per_game_2022': 24.1,
            'points_allowed_2022': 20.3
        },
        {
            'team_name': 'New York Giants',
            'off_rank_2022': 24,
            'def_rank_2022': 20,
            'points_per_game_2022': 20.8,
            'points_allowed_2022': 21.8
        },
        {
            'team_name': 'New York Jets',
            'off_rank_2022': 28,
            'def_rank_2022': 25,
            'points_per_game_2022': 18.5,
            'points_allowed_2022': 27.1
        },
        {
            'team_name': 'Philadelphia Eagles',
            'off_rank_2022': 22,
            'def_rank_2022': 21,
            'points_per_game_2022': 21.3,
            'points_allowed_2022': 23.9
        },
        {
            'team_name': 'Pittsburgh Steelers',
            'off_rank_2022': 16,
            'def_rank_2022': 10,
            'points_per_game_2022': 24.9,
            'points_allowed_2022': 20.9
        },
        {
            'team_name': 'San Francisco 49ers',
            'off_rank_2022': 12,
            'def_rank_2022': 11,
            'points_per_game_2022': 25.4,
            'points_allowed_2022': 21.8
        },
        {
            'team_name': 'Seattle Seahawks',
            'off_rank_2022': 7,
            'def_rank_2022': 27,
            'points_per_game_2022': 27.3,
            'points_allowed_2022': 24.5
        },
        {
            'team_name': 'Tampa Bay Buccaneers',
            'off_rank_2022': 4,
            'def_rank_2022': 18,
            'points_per_game_2022': 30.1,
            'points_allowed_2022': 22.8
        },
        {
            'team_name': 'Tennessee Titans',
            'off_rank_2022': 15,
            'def_rank_2022': 23,
            'points_per_game_2022': 25.8,
            'points_allowed_2022': 24.2
        },
        {
            'team_name': 'Washington Football Team',
            'off_rank_2022': 20,
            'def_rank_2022': 13,
            'points_per_game_2022': 22.6,
            'points_allowed_2022': 22.2
        }
    ]


    for team_data in teams_data:
        team = Team(**team_data)
        db.session.add(team)

    # Create games
    games_data = [
    {
        'date_time': '2023-09-10 20:20',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Jacksonville Jaguars vs. Houston Texans'
    },
    {
        'date_time': '2023-09-10 20:20',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Kansas City Chiefs vs. Cleveland Browns'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'Bank of America Stadium, Charlotte, NC',
        'matchup': 'Carolina Panthers vs. New York Jets'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Atlanta Falcons vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'New York Giants vs. Denver Broncos'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'FedExField, Landover, MD',
        'matchup': 'Washington Football Team vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Detroit Lions vs. Green Bay Packers'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Indianapolis Colts vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New England Patriots vs. Miami Dolphins'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Baltimore Ravens vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-09-11 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'New Orleans Saints vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-09-11 16:25',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Rams vs. Chicago Bears'
    },
    {
        'date_time': '2023-09-11 16:25',
        'location': 'State Farm Stadium, Glendale, AZ',
        'matchup': 'Arizona Cardinals vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-09-11 16:25',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Denver Broncos vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-09-11 20:20',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Las Vegas Raiders vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-09-11 20:20',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Seattle Seahawks vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-09-11 20:20',
        'location': 'State Farm Stadium, Glendale, AZ',
        'matchup': 'Arizona Cardinals vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-09-12 20:15',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New England Patriots vs. Buffalo Bills'
    },
    {
        'date_time': '2023-09-12 20:15',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tampa Bay Buccaneers vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-09-15 20:20',
        'location': 'Paul Brown Stadium, Cincinnati, OH',
        'matchup': 'Cincinnati Bengals vs. Cleveland Browns'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'Bank of America Stadium, Charlotte, NC',
        'matchup': 'Carolina Panthers vs. New Orleans Saints'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Indianapolis Colts vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Atlanta Falcons vs. Washington Football Team'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'New Orleans Saints vs. New York Giants'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Baltimore Ravens vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Pittsburgh Steelers vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-09-17 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Detroit Lions vs. Green Bay Packers'
    },
    {
        'date_time': '2023-09-17 16:05',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Rams vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-09-17 16:25',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Seattle Seahawks vs. Tennessee Titans'
    },
    {
        'date_time': '2023-09-17 20:20',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New England Patriots vs. Dallas Cowboys'
            },
    {
        'date_time': '2023-09-18 20:15',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Jacksonville Jaguars vs. Miami Dolphins'
    },
    {
        'date_time': '2023-09-22 20:20',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Denver Broncos vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'Bank of America Stadium, Charlotte, NC',
        'matchup': 'Carolina Panthers vs. Washington Football Team'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Indianapolis Colts vs. Tennessee Titans'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Atlanta Falcons vs. New York Giants'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'New Orleans Saints vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Baltimore Ravens vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Pittsburgh Steelers vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-09-24 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Detroit Lions vs. Chicago Bears'
    },
    {
        'date_time': '2023-09-24 16:05',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Rams vs. Arizona Cardinals'
    },
    {
        'date_time': '2023-09-24 16:25',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Seattle Seahawks vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-09-24 20:20',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New England Patriots vs. New York Jets'
    },
    {
        'date_time': '2023-09-25 20:15',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tampa Bay Buccaneers vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-09-28 20:15',
        'location': 'Lambeau Field, Green Bay, WI',
        'matchup': 'Detroit Lions vs. Green Bay Packers'
    },
    {
        'date_time': '2023-10-01 09:30',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Atlanta Falcons vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'Miami Dolphins vs. Buffalo Bills'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'Bank of America Stadium, Charlotte, NC',
        'matchup': 'Minnesota Vikings vs. Carolina Panthers'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Denver Broncos vs. Chicago Bears'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Baltimore Ravens vs. Cleveland Browns'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Pittsburgh Steelers vs. Houston Texans'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Rams vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tampa Bay Buccaneers vs. New Orleans Saints'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'FedExField, Landover, MD',
        'matchup': 'Washington Commanders vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-10-01 13:00',
        'location': 'Paul Brown Stadium, Cincinnati, OH',
        'matchup': 'Cincinnati Bengals vs. Tennessee Titans'
    },
    {
        'date_time': '2023-10-01 16:05',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Las Vegas Raiders vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-10-01 16:25',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New England Patriots vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-10-01 16:25',
        'location': 'State Farm Stadium, Glendale, AZ',
        'matchup': 'Arizona Cardinals vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-10-01 20:20',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Kansas City Chiefs vs. New York Jets'
    },
    {
        'date_time': '2023-10-02 20:15',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Seattle Seahawks vs. New York Giants'
    },
    {
        'date_time': '2023-10-05 20:15',
        'location': 'FedExField, Landover, MD',
        'matchup': 'Chicago Bears vs. Washington Commanders'
    },
    {
        'date_time': '2023-10-08 09:30',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'Jacksonville Jaguars vs. Buffalo Bills'
    },
    {
        'date_time': '2023-10-08 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Houston Texans vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-10-08 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Carolina Panthers vs. Detroit Lions'
    },
    {
        'date_time': '2023-10-08 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Tennessee Titans vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-10-08 13:00',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'New York Giants vs. Miami Dolphins'
    },
    {
        'date_time': '2023-10-08 13:00',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New Orleans Saints vs. New England Patriots'
    },
    {
        'date_time': '2023-10-08 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Baltimore Ravens vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-10-08 16:05',
        'location': 'State Farm Stadium, Glendale, AZ',
        'matchup': 'Cincinnati Bengals vs. Arizona Cardinals'
    },
    {
        'date_time': '2023-10-08 16:05',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Philadelphia Eagles vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-10-08 16:25',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'New York Jets vs. Denver Broncos'
    },
    {
        'date_time': '2023-10-08 16:25',
        'location': 'U.S. Bank Stadium, Minneapolis, MN',
        'matchup': 'Kansas City Chiefs vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-10-08 20:20',
        'location': 'Levi\'s Stadium, Santa Clara, CA',
        'matchup': 'Dallas Cowboys vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-10-09 20:15',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Green Bay Packers vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-10-12 20:15',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Denver Broncos vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-10-15 09:30',
        'location': 'Nissan Stadium, Nashville, TN',
        'matchup': 'Baltimore Ravens vs. Tennessee Titans'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Washington Commanders vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Minnesota Vikings vs. Chicago Bears'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'Paul Brown Stadium, Cincinnati, OH',
        'matchup': 'Seattle Seahawks vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'FirstEnergy Stadium, Cleveland, OH',
        'matchup': 'San Francisco 49ers vs. Cleveland Browns'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'NRG Stadium, Houston, TX',
        'matchup': 'New Orleans Saints vs. Houston Texans'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Indianapolis Colts vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Carolina Panthers vs. Miami Dolphins'
    },
    {
        'date_time': '2023-10-15 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Detroit Lions vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-10-15 16:05',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'New England Patriots vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-10-15 16:25',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Arizona Cardinals vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-10-15 16:25',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Philadelphia Eagles vs. New York Jets'
    },
    {
        'date_time': '2023-10-15 20:20',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'New York Giants vs. Buffalo Bills'
    },
    {
        'date_time': '2023-10-16 20:15',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Dallas Cowboys vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-10-19 20:15',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'Jacksonville Jaguars vs. New Orleans Saints'
    },
    {
        'date_time': '2023-10-22 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Baltimore Ravens vs. Detroit Lions'
    },
    {
        'date_time': '2023-10-22 13:00',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Chicago Bears vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-10-22 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Cleveland Browns vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-10-22 13:00',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'Buffalo Bills vs. New England Patriots'
    },
    {
        'date_time': '2023-10-22 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Washington Commanders vs. New York Giants'
    },
    {
        'date_time': '2023-10-22 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Atlanta Falcons vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-10-22 16:05',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Pittsburgh Steelers vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-10-22 16:05',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Arizona Cardinals vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-10-22 16:25',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Green Bay Packers vs. Denver Broncos'
    },
    {
        'date_time': '2023-10-22 16:25',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Los Angeles Chargers vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-10-22 20:20',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Philadelphia Eagles vs. Miami Dolphins'
    },
    {
        'date_time': '2023-10-23 20:15',
        'location': 'U.S. Bank Stadium, Minneapolis, MN',
        'matchup': 'San Francisco 49ers vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-10-26 20:15',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Buffalo Bills vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'NRG Stadium, Houston, TX',
        'matchup': 'Carolina Panthers vs. Houston Texans'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Dallas Cowboys vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'U.S. Bank Stadium, Minneapolis, MN',
        'matchup': 'Green Bay Packers vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'Indianapolis Colts vs. New Orleans Saints'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'Miami Dolphins vs. New England Patriots'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'New York Giants vs. New York Jets'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Jacksonville Jaguars vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Tennessee Titans vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-10-29 13:00',
        'location': 'Lincoln Financial Field, Philadelphia, PA',
        'matchup': 'Washington Commanders vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-10-29 16:05',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Cleveland Browns vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-10-29 16:25',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Arizona Cardinals vs. Baltimore Ravens'
    },
    {
        'date_time': '2023-10-29 16:25',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Denver Broncos vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-10-29 16:25',
        'location': 'Paul Brown Stadium, Cincinnati, OH',
        'matchup': 'San Francisco 49ers vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-10-29 20:20',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Los Angeles Chargers vs. Chicago Bears'
    },
    {
        'date_time': '2023-10-30 20:15',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Detroit Lions vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-11-02 20:15',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Tennessee Titans vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-11-05 09:30',
        'location': 'Tottenham Hotspur Stadium, London, England',
        'matchup': 'Kansas City Chiefs vs. Miami Dolphins'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Minnesota Vikings vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Seattle Seahawks vs. Baltimore Ravens'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'FirstEnergy Stadium, Cleveland, OH',
        'matchup': 'Arizona Cardinals vs. Cleveland Browns'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'Lambeau Field, Green Bay, WI',
        'matchup': 'Los Angeles Rams vs. Green Bay Packers'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Houston Texans vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'Washington Commanders vs. New England Patriots'
    },
    {
        'date_time': '2023-11-05 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'Chicago Bears vs. New Orleans Saints'
    },
    {
        'date_time': '2023-11-05 16:05',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Carolina Panthers vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-11-05 16:25',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'New York Giants vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-11-05 16:25',
        'location': 'AT&T Stadium, Arlington, TX',
        'matchup': 'Philadelphia Eagles vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-11-05 20:20',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'Cincinnati Bengals vs. Buffalo Bills'
    },
    {
        'date_time': '2023-11-06 20:15',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'New York Jets vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-11-09 20:15',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Carolina Panthers vs. Chicago Bears'
    },
    {
        'date_time': '2023-11-12 09:30',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'Indianapolis Colts vs. New England Patriots'
    },
    {
        'date_time': '2023-11-12 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Cleveland Browns vs. Baltimore Ravens'
    },
    {
        'date_time': '2023-11-12 13:00',
        'location': 'Paul Brown Stadium, Cincinnati, OH',
        'matchup': 'Houston Texans vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-11-12 13:00',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'San Francisco 49ers vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-11-12 13:00',
        'location': 'U.S. Bank Stadium, Minneapolis, MN',
        'matchup': 'New Orleans Saints vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-11-12 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Green Bay Packers vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-11-12 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tennessee Titans vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-11-12 16:05',
        'location': 'State Farm Stadium, Glendale, AZ',
        'matchup': 'Atlanta Falcons vs. Arizona Cardinals'
    },
    {
        'date_time': '2023-11-12 16:05',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Los Angeles Chargers vs. Detroit Lions'
    },
    {
        'date_time': '2023-11-12 16:25',
        'location': 'AT&T Stadium, Arlington, TX',
        'matchup': 'New York Giants vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-11-12 16:25',
        'location': 'FedExField, Landover, MD',
        'matchup': 'Washington Commanders vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-11-12 20:20',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'New York Jets vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-11-13 20:15',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Denver Broncos vs. Buffalo Bills'
    },
    {
        'date_time': '2023-11-16 20:15',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Cincinnati Bengals vs. Baltimore Ravens'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'Bank of America Stadium, Charlotte, NC',
        'matchup': 'Dallas Cowboys vs. Carolina Panthers'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'FirstEnergy Stadium, Cleveland, OH',
        'matchup': 'Pittsburgh Steelers vs. Cleveland Browns'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Chicago Bears vs. Detroit Lions'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Chargers vs. Green Bay Packers'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'NRG Stadium, Houston, TX',
        'matchup': 'Arizona Cardinals vs. Houston Texans'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Tennessee Titans vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'Allegiant Stadium, Paradise, NV',
        'matchup': 'Las Vegas Raiders vs. Miami Dolphins'
    },
    {
        'date_time': '2023-11-19 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'New York Giants vs. Washington Commanders'
    },
    {
        'date_time': '2023-11-19 16:05',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tampa Bay Buccaneers vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-11-19 16:25',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'New York Jets vs. Buffalo Bills'
    },
    {
        'date_time': '2023-11-19 16:25',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Seattle Seahawks vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-11-19 20:20',
        'location': 'U.S. Bank Stadium, Minneapolis, MN',
        'matchup': 'Minnesota Vikings vs. Denver Broncos'
    },
    {
        'date_time': '2023-11-20 20:15',
        'location': 'Lincoln Financial Field, Philadelphia, PA',
        'matchup': 'Philadelphia Eagles vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-11-23 12:30',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Green Bay Packers vs. Detroit Lions'
    },
    {
        'date_time': '2023-11-23 16:30',
        'location': 'AT&T Stadium, Arlington, TX',
        'matchup': 'Washington Commanders vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-11-23 20:20',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'San Francisco 49ers vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-11-24 15:00',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Miami Dolphins vs. New York Jets'
    },
    {
        'date_time': '2023-11-26 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'New Orleans Saints vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-11-26 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Pittsburgh Steelers vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-11-26 13:00',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Jacksonville Jaguars vs. Houston Texans'
    },
    {
        'date_time': '2023-11-26 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tampa Bay Buccaneers vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-11-26 13:00',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'New England Patriots vs. New York Giants'
    },
    {
        'date_time': '2023-11-26 13:00',
        'location': 'Bank of America Stadium, Charlotte, NC',
        'matchup': 'Carolina Panthers vs. Tennessee Titans'
    },
    {
        'date_time': '2023-11-26 16:05',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Rams vs. Arizona Cardinals'
    },
    {
        'date_time': '2023-11-26 16:05',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Cleveland Browns vs. Denver Broncos'
    },
    {
        'date_time': '2023-11-26 16:25',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Kansas City Chiefs vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-11-26 16:25',
        'location': 'Bills Stadium, Orchard Park, NY',
        'matchup': 'Buffalo Bills vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-11-26 20:20',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Baltimore Ravens vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-11-27 20:15',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Chicago Bears vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-11-30 20:15',
        'location': 'AT&T Stadium, Arlington, TX',
        'matchup': 'Seattle Seahawks vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'New England Patriots vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'Detroit Lions vs. New Orleans Saints'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Atlanta Falcons vs. New York Jets'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Pittsburgh Steelers vs. Arizona Cardinals'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'Tampa Bay Buccaneers vs. Carolina Panthers'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Tennessee Titans vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-12-03 13:00',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Washington Commanders vs. Miami Dolphins'
    },
    {
        'date_time': '2023-12-03 16:05',
        'location': 'NRG Stadium, Houston, TX',
        'matchup': 'Houston Texans vs. Denver Broncos'
    },
    {
        'date_time': '2023-12-03 16:25',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Rams vs. Cleveland Browns'
    },
    {
        'date_time': '2023-12-03 16:25',
        'location': 'Lincoln Financial Field, Philadelphia, PA',
        'matchup': 'Philadelphia Eagles vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-12-03 20:20',
        'location': 'Lambeau Field, Green Bay, WI',
        'matchup': 'Green Bay Packers vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-12-04 20:15',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Jacksonville Jaguars vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-12-07 20:15',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'New England Patriots vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'Mercedes-Benz Stadium, Atlanta, GA',
        'matchup': 'Tampa Bay Buccaneers vs. Atlanta Falcons'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'M&T Bank Stadium, Baltimore, MD',
        'matchup': 'Los Angeles Rams vs. Baltimore Ravens'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Detroit Lions vs. Chicago Bears'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'Paul Brown Stadium, Cincinnati, OH',
        'matchup': 'Indianapolis Colts vs. Cincinnati Bengals'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'FirstEnergy Stadium, Cleveland, OH',
        'matchup': 'Jacksonville Jaguars vs. Cleveland Browns'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'Carolina Panthers vs. New Orleans Saints'
    },
    {
        'date_time': '2023-12-10 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'New York Jets vs. Houston Texans'
    },
    {
        'date_time': '2023-12-10 16:05',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Las Vegas Raiders vs. Minnesota Vikings'
    },
    {
        'date_time': '2023-12-10 16:05',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'San Francisco 49ers vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-12-10 16:25',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'Kansas City Chiefs vs. Buffalo Bills'
    },
    {
        'date_time': '2023-12-10 16:25',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Los Angeles Chargers vs. Denver Broncos'
    },
    {
        'date_time': '2023-12-10 20:20',
        'location': 'Lincoln Financial Field, Philadelphia, PA',
        'matchup': 'Dallas Cowboys vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-12-11 20:15',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Miami Dolphins vs. Tennessee Titans'
    },
    {
        'date_time': '2023-12-11 20:15',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Green Bay Packers vs. New York Giants'
    },
    {
        'date_time': '2023-12-14 20:15',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Los Angeles Chargers vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-12-17 13:00',
        'location': 'Lambeau Field, Green Bay, WI',
        'matchup': 'Tampa Bay Buccaneers vs. Green Bay Packers'
    },
    {
        'date_time': '2023-12-17 13:00',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'New York Jets vs. Miami Dolphins'
    },
    {
        'date_time': '2023-12-17 13:00',
        'location': 'Mercedes-Benz Superdome, New Orleans, LA',
        'matchup': 'New York Giants vs. New Orleans Saints'
    },
    {
        'date_time': '2023-12-17 13:00',
        'location': 'Nissan Stadium, Nashville, TN',
        'matchup': 'Houston Texans vs. Tennessee Titans'
    },
    {
        'date_time': '2023-12-17 16:05',
        'location': 'State Farm Stadium, Glendale, AZ',
        'matchup': 'San Francisco 49ers vs. Arizona Cardinals'
    },
    {
        'date_time': '2023-12-17 16:05',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'Washington Commanders vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-12-17 16:25',
        'location': 'Highmark Stadium, Orchard Park, NY',
        'matchup': 'Dallas Cowboys vs. Buffalo Bills'
    },
    {
        'date_time': '2023-12-17 16:25',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Philadelphia Eagles vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-12-17 20:20',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Baltimore Ravens vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-12-18 20:15',
        'location': 'Gillette Stadium, Foxborough, MA',
        'matchup': 'Kansas City Chiefs vs. New England Patriots'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Atlanta Falcons vs. Carolina Panthers'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Minnesota Vikings vs. Cincinnati Bengals'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Chicago Bears vs. Cleveland Browns'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Denver Broncos vs. Detroit Lions'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Pittsburgh Steelers vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-12-21 20:15',
        'location': 'SoFi Stadium, Inglewood, CA',
        'matchup': 'New Orleans Saints vs. Los Angeles Rams'
    },
    {
        'date_time': '2023-12-23 16:30',
        'location': 'Heinz Field, Pittsburgh, PA',
        'matchup': 'Cincinnati Bengals vs. Pittsburgh Steelers'
    },
    {
        'date_time': '2023-12-23 20:00',
        'location': 'Bills Stadium, Orchard Park, NY',
        'matchup': 'Buffalo Bills vs. Los Angeles Chargers'
    },
    {
        'date_time': '2023-12-24 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Atlanta Falcons vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-12-24 13:00',
        'location': 'Lambeau Field, Green Bay, WI',
        'matchup': 'Carolina Panthers vs. Green Bay Packers'
    },
    {
        'date_time': '2023-12-24 13:00',
        'location': 'NRG Stadium, Houston, TX',
        'matchup': 'Cleveland Browns vs. Houston Texans'
    },
    {
        'date_time': '2023-12-24 13:00',
        'location': 'Ford Field, Detroit, MI',
        'matchup': 'Minnesota Vikings vs. Detroit Lions'
    },
    {
        'date_time': '2023-12-24 13:00',
        'location': 'FedExField, Landover, MD',
        'matchup': 'New York Jets vs. Washington Commanders'
    },
    {
        'date_time': '2023-12-24 13:00',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Tennessee Titans vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-12-24 16:05',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Tampa Bay Buccaneers vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-12-24 16:25',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Arizona Cardinals vs. Chicago Bears'
    },
    {
        'date_time': '2023-12-24 16:25',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Dallas Cowboys vs. Miami Dolphins'
    },
    {
        'date_time': '2023-12-25 20:15',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'New England Patriots vs. Denver Broncos'
    },
    {
        'date_time': '2023-12-25 13:00',
        'location': 'Allegiant Stadium, Las Vegas, NV',
        'matchup': 'Kansas City Chiefs vs. Las Vegas Raiders'
    },
    {
        'date_time': '2023-12-25 16:30',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Philadelphia Eagles vs. New York Giants'
    },
    {
        'date_time': '2023-12-25 20:15',
        'location': 'Levi\'s Stadium, Santa Clara, CA',
        'matchup': 'Baltimore Ravens vs. San Francisco 49ers'
    },
    {
        'date_time': '2023-12-28 20:15',
        'location': 'FirstEnergy Stadium, Cleveland, OH',
        'matchup': 'New York Jets vs. Cleveland Browns'
    },
    {
        'date_time': '2023-12-30 20:15',
        'location': 'AT&T Stadium, Arlington, TX',
        'matchup': 'Detroit Lions vs. Dallas Cowboys'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Hard Rock Stadium, Miami Gardens, FL',
        'matchup': 'Miami Dolphins vs. Baltimore Ravens'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Bills Stadium, Orchard Park, NY',
        'matchup': 'New England Patriots vs. Buffalo Bills'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Soldier Field, Chicago, IL',
        'matchup': 'Atlanta Falcons vs. Chicago Bears'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'NRG Stadium, Houston, TX',
        'matchup': 'Tennessee Titans vs. Houston Texans'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Lucas Oil Stadium, Indianapolis, IN',
        'matchup': 'Las Vegas Raiders vs. Indianapolis Colts'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'TIAA Bank Field, Jacksonville, FL',
        'matchup': 'Carolina Panthers vs. Jacksonville Jaguars'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'MetLife Stadium, East Rutherford, NJ',
        'matchup': 'Los Angeles Rams vs. New York Giants'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Lincoln Financial Field, Philadelphia, PA',
        'matchup': 'Arizona Cardinals vs. Philadelphia Eagles'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Raymond James Stadium, Tampa, FL',
        'matchup': 'New Orleans Saints vs. Tampa Bay Buccaneers'
    },
    {
        'date_time': '2023-12-31 13:00',
        'location': 'Levi\'s Stadium, Santa Clara, CA',
        'matchup': 'San Francisco 49ers vs. Washington Commanders'
    },
    {
        'date_time': '2023-12-31 16:05',
        'location': 'Lumen Field, Seattle, WA',
        'matchup': 'Pittsburgh Steelers vs. Seattle Seahawks'
    },
    {
        'date_time': '2023-12-31 16:25',
        'location': 'Empower Field at Mile High, Denver, CO',
        'matchup': 'Los Angeles Chargers vs. Denver Broncos'
    },
    {
        'date_time': '2023-12-31 16:25',
        'location': 'Arrowhead Stadium, Kansas City, MO',
        'matchup': 'Cincinnati Bengals vs. Kansas City Chiefs'
    },
    {
        'date_time': '2023-12-31 20:20',
        'location': 'U.S. Bank Stadium, Minneapolis, MN',
        'matchup': 'Green Bay Packers vs. Minnesota Vikings'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Seattle Seahawks vs. Arizona Cardinals'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Pittsburgh Steelers vs. Baltimore Ravens'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Tampa Bay Buccaneers vs. Carolina Panthers'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Cleveland Browns vs. Cincinnati Bengals'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Minnesota Vikings vs. Detroit Lions'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Chicago Bears vs. Green Bay Packers'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Houston Texans vs. Indianapolis Colts'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Kansas City Chiefs vs. Los Angeles Chargers'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Denver Broncos vs. Las Vegas Raiders'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Buffalo Bills vs. Miami Dolphins'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'New York Jets vs. New England Patriots'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Atlanta Falcons vs. New Orleans Saints'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Philadelphia Eagles vs. New York Giants'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Los Angeles Rams vs. San Francisco 49ers'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Jacksonville Jaguars vs. Tennessee Titans'
    },
    {
        'date_time': 'TBD',
        'location': 'TBD',
        'matchup': 'Dallas Cowboys vs. Washington Commanders'
    }
]



    for game_data in games_data:
        game = Game(**game_data)
        db.session.add(game)

    db.session.commit()
    print("🌱 Hotels, Customers, and Reviews successfully seeded! 🌱")
