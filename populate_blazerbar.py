import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blazerbar_project.settings')

import django
django.setup()

from blazerbar.models import Game, Rating, Bar, Favorite, User

def populate():
	alex = User.objects.get(username='alex')
	guest = User.objects.get(username='guest')
	stormbreaker_bar = add_bar('Stormbreaker Brewing', 'Mississippi and Fremont', 'N', 'XL', True, False)
	add_rating(alex, stormbreaker_bar, rating=8, review='Busy on a sunny day but a nice outdoor setup')
	add_rating(guest, stormbreaker_bar, rating=5, review='bad service, not worth the screen')
	migration_bar = add_bar('Migration Brewing', 'Glisan and 30th', 'NE', 'M', True, True)
	add_rating(alex, migration_bar, rating=7, review='busy busy busy')
	add_rating(guest, migration_bar, rating=9, review="Terry's Porter")
	sweethereafter_bar = add_bar('Sweet Hereafter', 'Belmont and 33rd', 'SE', 'XL', True, False)
	cheerfultortoise_bar = add_bar('The Cheerful Tortoise', 'Broadway and College', 'SW', 'L', True, True)
	highdive_bar = add_bar('The High Dive', '12th and Hawthorne', 'SE', 'L', True, False)
	add_rating(alex, highdive_bar, rating=9, review='good service, good beer, easy to find a seat')
	exnovo_bar = add_bar('Ex-Novo Brewing', 'Russel and Mississippi', 'NE', 'M', True, False)
	add_rating(alex, exnovo_bar, rating=8, review='Damon Stoutamaire. Near the Rose Quarter')
	add_favorite(alex, stormbreaker_bar)
	add_favorite(alex, sweethereafter_bar)
	add_favorite(guest, migration_bar)
	add_favorite(guest, highdive_bar)



def add_bar(name, location, neighborhood, tvsize, sound, happyhour):
	b =  Bar.objects.get_or_create(name=name)[0]
	b.location = location
	b.neighborhood = neighborhood
	b.tv_size = tvsize
	b.sound = sound
	b.happyhour_hour = happyhour
	b.save()
	return b

def add_rating(user, bar, rating, review):
	r = Rating.objects.get_or_create(bar=bar, user=user, rating=rating, review=review)[0]
	#r.rating = rating
	#r.review = review
	r.save()
	return r

#def add_game(bar, user, date):
#	g = Game.objects.get_or_create(bar=bar, user=user)
#	g.date = date
#	g.save()
#	g.bar.save()
#	return g


# built-in function to increment likes and favorites is probably very wrong.
def add_favorite(user, bar):
	f = Favorite.objects.get_or_create(user=user, bar=bar)[0]
	f.bar.favorites += 1
	f.save()
	f.bar.save()
	return f

if __name__ == '__main__':
    print "Starting Blazerbar population script..."
    populate()


