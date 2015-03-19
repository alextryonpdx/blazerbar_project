import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blazerbar_project.settings')

import django
django.setup()

from blazerbar.models import Game, Team

def add_game(home_team, away_team, game_date, game_id):
	print home_team + " vs " + away_team + " on " + game_date
	identifier = home_team + game_date
	g = Game.objects.get_or_create(game_id=game_id)[0]
	g.home_team = home_team
	g.away_team = away_team
	g.game_date = game_date
	team1 = Team.objects.get(full_name=home_team)
	team2 = Team.objects.get(full_name=away_team)
	g.teams.add(team1)
	g.teams.add(team2)
	g.save()
	return g


f = open('blazerbar/sports_data/schedule.txt', 'r')
data = json.load(f)
for i in range(len(data["games"])):
	home_team = data["games"][i]["home"]["name"]
	away_team = data["games"][i]["away"]["name"]
	game_date = data["games"][i]["scheduled"]
	game_id = data["games"][i]["id"]
	add_game(home_team, away_team, game_date, game_id)
	#year = data["games"][i]["scheduled"][:4]
	#month = data["games"][i]["scheduled"][5:7]
	#day = data["games"][i]["scheduled"][8:10]

#year = game_date[:4]
#month = game_date[5:7]
#day = game_date[8:10]
