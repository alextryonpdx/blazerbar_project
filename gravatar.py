# import code for encoding urls and generating md5 hashes
import urllib, hashlib
 
"""
# Set your variables here
email = "someone@somewhere.com"
default = "http://www.example.com/default.jpg"
size = 40
 
# construct the url
gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
gravatar_url += ".json"
"""


def get_gravatar_url(user_email):
	email = user_email
	default = "http://www.example.com/default.jpg"
	size = 40
 
	# construct the url
	gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
	gravatar_url += urllib.urlencode({'d':default, 's':str(size)})
	#gravatar_url += ".json"
	return gravatar_url
