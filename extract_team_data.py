import json
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blazerbar_project.settings')

import django
django.setup()

from blazerbar.models import Team

def add_team(league, conference, division, name, market, alias, team_id):
	print name
	full_name = market + " " + name
	t = Team.objects.get_or_create(team_id=team_id)[0]
	t.full_name = full_name
	t.name = name
	t.market = market
	t.league = league
	t.conference = conference
	t.division = division
	abbr_name = alias + " " + league
	t.abbr_name = abbr_name
	t.save()
	return t

f = open('blazerbar/sports_data/nbateams.txt', 'r')
data = json.load(f)
league = "NBA"
for c in data["conferences"]:
	conference = c["name"]
	print conference
	for d in c["divisions"]:
		division = d["name"]
		print division
		for t in d["teams"]:
			name = t["name"]
			market = t["market"]
			alias = t["alias"]
			team_id = t["id"]
			add_team(league, conference, division, name, market, alias, team_id)
	


""" NOT RIGHT BUT KINDA GOT THE STEPS
for con in data:
	conference = data["conferences"][con]["name"]
	print conference
for c in l:
	print c["name"]
	conference = c["name"]
	for d in c["divisions"]:
		division = d["name"]
		for t in d["teams"]:
			name = t["name"]
			market = t["market"]
			alias = t["alias"]
			add_team(league, conference, division, name, market, alias)"""











