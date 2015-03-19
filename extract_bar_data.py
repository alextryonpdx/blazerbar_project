import json
import os
from django.template.defaultfilters import slugify
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blazerbar_project.settings')

import django
django.setup()

from blazerbar.models import Bar

def add_bar(name, location, image_url, tvsize, sound, happyhour):
	print name
	b =  Bar.objects.get_or_create(name=name)[0]
	b.location = location
	b.image_url = image_url
	#b.neighborhood = neighborhood
	b.bar_slug = slugify(name)
	b.tv_size = tvsize
	b.sound = sound
	b.happyhour_hour = happyhour
	b.save()
	return b

for i in range(13):
	f = open('blazerbar/yelp-data/results'+ str(i+1) +'.txt', 'r')
	getback = json.load(f)
	for biz in getback:
		name = biz['name']
		location = biz['location']['address'][0]
		image_url = biz['image_url']
		add_bar(name, location, image_url, "","","")


